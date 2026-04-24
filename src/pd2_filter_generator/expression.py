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
E = TypeVar("E", bound="Node")


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


class ExprMixin(Generic[E]):
    """Mixin for expression nodes."""

    # Cannot extend ABC - otherwise we will get metaclass conflict
    @abstractmethod
    def as_node(self) -> "E":
        raise NotImplementedError

    # We have to block == and != default methods.
    # Other operations are defined to raise TypeError (not AttributeError) to make errors more explicit.

    def __hash__(self):
        msg = f"Cannot hash {type(self).__name__}"
        raise TypeError(msg)

    def __eq__(self, other: object) -> "BoolExpr":  # type: ignore[override]
        msg = f"Cannot use == with {type(self).__name__}"
        raise TypeError(msg)

    def __ne__(self, other: object) -> "BoolExpr":  # type: ignore[override]
        msg = f"Cannot use != with {type(self).__name__}"
        raise TypeError(msg)


class BoolMixin(ExprMixin["BoolExpr"]):
    """Mixin counterpart to BoolExpr — supports ~, &, | operators."""

    def __invert__(self) -> "BoolExpr":
        return Not(self)

    def __and__(self, other: "BoolMixin") -> "BoolExpr":
        return And(self, other)

    def __or__(self, other: "BoolMixin") -> "BoolExpr":
        return Or(self, other)


class IntMixin(ExprMixin["IntExpr"]):
    """Mixin counterpart to IntExpr — supports ==, !=, <, > operators."""

    def __hash__(self):
        msg = f"Cannot hash {type(self).__name__}"
        raise TypeError(msg)

    def __eq__(self, other: "IntMixin") -> "BoolExpr":  # type: ignore[override]
        return Equal(self, other)

    def __ne__(self, other: "IntMixin") -> "BoolExpr":  # type: ignore[override]
        return NotEqual(self, other)

    def __lt__(self, other: "IntMixin") -> "BoolExpr":
        return LessThan(self, other)

    def __gt__(self, other: "IntMixin") -> "BoolExpr":
        return GreaterThan(self, other)


class Node(ExprMixin["Node"], ABC):
    """Base class for expression tree nodes."""

    def as_node(self) -> "Node":
        return self

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


class BoolExpr(Node, BoolMixin, ABC):
    """Nodes representing boolean expressions. Support ~, &, | operators."""


class IntExpr(Node, IntMixin, ABC):
    """Nodes supporting ordering operators (==, !=, <, >)."""


class Leaf(Node, ABC):
    """Leaf node holding a value."""

    def __init__(self, value: str):
        super().__init__()
        self.value = value

    def accept(self, visitor: NodeVisitor[T]) -> T:
        return visitor.visit_literal(self.value)


class IntLit(Leaf, IntExpr):
    def __repr__(self):
        return f"IntLit({self.value})"


class IntRef(Leaf, IntExpr):
    def __repr__(self):
        return f"IntRef({self.value})"


class BoolRef(Leaf, BoolExpr):
    def __repr__(self):
        return f"BoolRef({self.value})"


class Not(BoolExpr):
    def __init__(self, operand: BoolMixin):
        self.operand = operand.as_node()
        if not isinstance(self.operand, BoolExpr):
            msg = f"~ requires BoolExpr, got {type(operand).__name__}"
            raise TypeError(msg)

    def accept(self, visitor: NodeVisitor[T]) -> T:
        operand = self.operand.accept(visitor)
        return visitor.visit_not(operand)

    def __repr__(self):
        return f"Not({self.operand})"


class BinaryOp(Node, ABC):
    def __init__(self, left: ExprMixin, right: ExprMixin):
        self.left = left.as_node()
        self.right = right.as_node()

        if not isinstance(self.left, self._operands_type) or not isinstance(self.right, self._operands_type):
            msg = f"{self.operator.symbol} requires {self._operands_type} operands, got {type(self.left).__name__} and {type(self.right).__name__}"
            raise TypeError(msg)

    @property
    @abstractmethod
    def operator(self) -> BinaryOperator:
        pass

    @property
    @abstractmethod
    def _operands_type(self) -> type:
        pass

    def accept(self, visitor: NodeVisitor[T]) -> T:
        left = self.left.accept(visitor)
        right = self.right.accept(visitor)
        return visitor.visit_binary_op(left, right, self.operator)

    def __repr__(self):
        return f"BinaryOp({self.left} {self.operator} {self.right})"


class LessThan(BinaryOp, BoolExpr):
    @property
    def operator(self) -> BinaryOperator:
        return BinaryOperator.LESS_THAN

    @property
    def _operands_type(self) -> type:
        return IntExpr


class GreaterThan(BinaryOp, BoolExpr):
    @property
    def operator(self) -> BinaryOperator:
        return BinaryOperator.GREATER_THAN

    @property
    def _operands_type(self) -> type:
        return IntExpr


class Equal(BinaryOp, BoolExpr):
    @property
    def operator(self) -> BinaryOperator:
        return BinaryOperator.EQUAL

    @property
    def _operands_type(self) -> type:
        return IntExpr


class NotEqual(BinaryOp, BoolExpr):
    @property
    def operator(self) -> BinaryOperator:
        return BinaryOperator.NOT_EQUAL

    @property
    def _operands_type(self) -> type:
        return IntExpr


class And(BinaryOp, BoolExpr):
    @property
    def operator(self) -> BinaryOperator:
        return BinaryOperator.AND

    @property
    def _operands_type(self) -> type:
        return BoolExpr


class Or(BinaryOp, BoolExpr):
    @property
    def operator(self) -> BinaryOperator:
        return BinaryOperator.OR

    @property
    def _operands_type(self) -> type:
        return BoolExpr
