"""Expression tree for PD2 filter conditions."""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Generic, TypeVar


class BinaryOperator(Enum):
    """Binary operators with precedence. Lower value = higher precedence (binds tighter)."""

    LESS_THAN = (1, "<")
    GREATER_THAN = (1, ">")
    EQUAL = (1, "=")
    NOT_EQUAL = (1, "!=")
    AND = (2, "AND")
    OR = (3, "OR")

    def __init__(self, precedence: int, symbol: str):
        self.precedence = precedence
        self.symbol = symbol


T = TypeVar("T")


class NodeVisitor(ABC, Generic[T]):
    @abstractmethod
    def visit_literal(self, value: str) -> T:
        pass

    @abstractmethod
    def visit_not(self, value: T) -> T:
        pass

    @abstractmethod
    def visit_binary_op(self, left: T, right: T, operator: BinaryOperator) -> T:
        pass


class Node(ABC):
    """Base class for expression tree nodes."""

    @abstractmethod
    def accept(self, visitor: NodeVisitor[T]) -> T:
        pass

    @abstractmethod
    def __repr__(self):
        pass

    def __bool__(self):
        msg = (
            f"Cannot use {type(self).__name__} in boolean context.\n"
            f"Expression nodes represent unevaluated conditions.\n"
            f"Use: & | ~ (not 'and' 'or' 'not')"
        )
        raise TypeError(msg)

    # We have to block == and != default methods.
    # Other operations are defined to raise TypeError (not AttributeError) to make errors more explicit.

    def __hash__(self):
        msg = f"Cannot hash {type(self).__name__}"
        raise TypeError(msg)

    def __invert__(self):
        self._raise_not_supported(type(self), "~")

    def __eq__(self, other):
        self._raise_not_supported(type(self), "==")

    def __ne__(self, other):
        self._raise_not_supported(type(self), "!=")

    def __lt__(self, other):
        self._raise_not_supported(type(self), "<")

    def __gt__(self, other):
        self._raise_not_supported(type(self), ">")

    @staticmethod
    def _raise_not_supported(node_type, operation: str):
        msg = f"Cannot use {operation} with {node_type.__name__}"
        raise TypeError(msg)


class EqNode(Node, ABC):  # noqa: PLW1641
    """Nodes that support equality comparison operators (==, !=)."""

    def __eq__(self, other: "EqNode") -> "BooleanNode":  # type: ignore[override]
        if not isinstance(other, EqNode):
            msg = f"Cannot use == with {type(other).__name__} (right operand does not support equality)"
            raise TypeError(msg)
        return Equal(self, other)

    def __ne__(self, other: "EqNode") -> "BooleanNode":  # type: ignore[override]
        if not isinstance(other, EqNode):
            msg = f"Cannot use != with {type(other).__name__} (right operand does not support equality)"
            raise TypeError(msg)
        return NotEqual(self, other)


class ComparableNode(EqNode, ABC):
    """Nodes that support ordering operators (<, >) in addition to equality (==, !=)."""

    def __lt__(self, other: "ComparableNode") -> "BooleanNode":
        if not isinstance(other, ComparableNode):
            msg = f"Cannot use < with {type(other).__name__} (right operand is not comparable)"
            raise TypeError(msg)
        return LessThan(self, other)

    def __gt__(self, other: "ComparableNode") -> "BooleanNode":
        if not isinstance(other, ComparableNode):
            msg = f"Cannot use > with {type(other).__name__} (right operand is not comparable)"
            raise TypeError(msg)
        return GreaterThan(self, other)


class BooleanNode(Node, ABC):
    """Nodes representing boolean expressions. Support boolean operators (~, &, |)."""

    def __invert__(self) -> "BooleanNode":
        return Not(self)

    def __and__(self, other: "BooleanNode") -> "BooleanNode":
        if not isinstance(other, BooleanNode):
            msg = f"Cannot use AND with {type(other).__name__} (right operand is not boolean)"
            raise TypeError(msg)
        return And(self, other)

    def __or__(self, other: "BooleanNode") -> "BooleanNode":
        if not isinstance(other, BooleanNode):
            msg = f"Cannot use OR with {type(other).__name__} (right operand is not boolean)"
            raise TypeError(msg)
        return Or(self, other)


class Literal(Node):
    """Leaf node holding a value."""

    def __init__(self, value: str):
        if type(self) is Literal:
            msg = "Cannot instantiate Literal directly"
            raise TypeError(msg)
        self.value = value

    def accept(self, visitor: NodeVisitor[T]) -> T:
        return visitor.visit_literal(self.value)

    def __repr__(self):
        return f"Literal({self.value})"


class CodeLiteral(Literal, EqNode):
    pass


class IntLiteral(Literal, ComparableNode):
    pass


class BoolLiteral(Literal, BooleanNode):
    pass


class Not(BooleanNode):
    def __init__(self, operand: BooleanNode):
        super().__init__()
        self.operand = operand

    def accept(self, visitor: NodeVisitor[T]) -> T:
        operand = self.operand.accept(visitor)
        return visitor.visit_not(operand)

    def __repr__(self):
        return f"Not({self.operand})"


class BinaryOp(Node):
    def __init__(self, left: Node, right: Node, operator: BinaryOperator):
        if type(self) is BinaryOp:
            # we need at least 1 abstract method for ABC to block direct instantiation
            msg = "Cannot instantiate BinaryOp directly"
            raise TypeError(msg)

        self.left = left
        self.right = right
        self.operator = operator

    def accept(self, visitor: NodeVisitor[T]) -> T:
        left = self.left.accept(visitor)
        right = self.right.accept(visitor)
        return visitor.visit_binary_op(left, right, self.operator)

    def __repr__(self):
        return f"BinaryOp({self.left} {self.operator} {self.right})"


class LessThan(BinaryOp, BooleanNode):
    def __init__(self, left: ComparableNode, right: ComparableNode):
        super().__init__(left, right, BinaryOperator.LESS_THAN)


class GreaterThan(BinaryOp, BooleanNode):
    def __init__(self, left: Node, right: Node):
        super().__init__(left, right, BinaryOperator.GREATER_THAN)


class Equal(BinaryOp, BooleanNode):
    def __init__(self, left: Node, right: Node):
        super().__init__(left, right, BinaryOperator.EQUAL)


class NotEqual(BinaryOp, BooleanNode):
    def __init__(self, left: Node, right: Node):
        super().__init__(left, right, BinaryOperator.NOT_EQUAL)


class And(BinaryOp, BooleanNode):
    def __init__(self, left: Node, right: Node):
        super().__init__(left, right, BinaryOperator.AND)


class Or(BinaryOp, BooleanNode):
    def __init__(self, left: Node, right: Node):
        super().__init__(left, right, BinaryOperator.OR)
