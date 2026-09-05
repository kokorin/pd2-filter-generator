"""Expression tree for PD2 filter conditions."""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Generic, TypeVar

T = TypeVar("T")


class NodeVisitor(ABC, Generic[T]):
    @abstractmethod
    def visit_literal(self, value: str) -> T:
        pass

    @abstractmethod
    def visit_not(self, value: T) -> T:
        pass

    @abstractmethod
    def visit_binary_op(self, left: T, right: T, operator: "BinaryOperator") -> T:
        pass


class ExprNode(ABC):
    """Base class for expression tree nodes."""

    @abstractmethod
    def accept(self, visitor: "NodeVisitor[T]") -> T:
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

    def __hash__(self):
        raise TypeError(f"Cannot hash {type(self).__name__}")

    def __invert__(self) -> "BoolExpr":
        raise TypeError(f"Cannot invert {type(self).__name__}")

    def __eq__(self, other: "ExprNode") -> "BoolExpr":  # type: ignore[override]
        return Equal(self, other)

    def __ne__(self, other: "ExprNode") -> "BoolExpr":  # type: ignore[override]
        return NotEqual(self, other)

    def __lt__(self, other: "ExprNode") -> "BoolExpr":
        return LessThan(self, other)

    def __gt__(self, other: "ExprNode") -> "BoolExpr":
        return GreaterThan(self, other)

    def __and__(self, other: "ExprNode") -> "BoolExpr":
        return And(self, other)

    def __or__(self, other: "ExprNode") -> "BoolExpr":
        return Or(self, other)


class BoolExpr(ExprNode, ABC):
    """Nodes representing boolean expressions. Support ~, &, | operators."""

    def __invert__(self) -> "BoolExpr":
        return Not(self)


class IntExpr(ExprNode, ABC):
    """Nodes supporting ordering operators (==, !=, <, >)."""


class BinaryOperator(Enum):
    """Binary operators with precedence. Lower value = higher precedence (binds tighter)."""

    LESS_THAN = (1, "<", IntExpr)
    GREATER_THAN = (1, ">", IntExpr)
    EQUAL = (1, "=", IntExpr)
    NOT_EQUAL = (1, "!=", IntExpr)
    AND = (2, "AND", BoolExpr)
    OR = (3, "OR", BoolExpr)

    def __init__(self, precedence: int, symbol: str, expr_cls: type) -> None:
        self.precedence = precedence
        self.symbol = symbol
        self.expr_cls = expr_cls


class ExprLeaf(ExprNode, ABC):
    """Leaf node holding a value."""

    def __init__(self, value: str):
        self.value = value

    def accept(self, visitor: NodeVisitor[T]) -> T:
        return visitor.visit_literal(self.value)


class IntLit(ExprLeaf, IntExpr):
    def __repr__(self):
        return f"IntLit({self.value})"


class IntRef(ExprLeaf, IntExpr):
    def __repr__(self):
        return f"IntRef({self.value})"


class BoolRef(ExprLeaf, BoolExpr):
    def __repr__(self):
        return f"BoolRef({self.value})"


class Not(BoolExpr):
    def __init__(self, operand: BoolExpr):
        if not isinstance(operand, BoolExpr):
            raise TypeError(f"The operand {operand} is not of type BoolExpr")

        self.operand = operand

    def accept(self, visitor: NodeVisitor[T]) -> T:
        return visitor.visit_not(self.operand.accept(visitor))

    def __repr__(self):
        return f"Not({self.operand})"


class BinaryOp(ExprNode, ABC):
    def __init__(self, operator: BinaryOperator, left: ExprNode, right: ExprNode):
        if not isinstance(left, operator.expr_cls):
            raise TypeError(f"Left operand {left} is not of type {operator.expr_cls}")
        if not isinstance(right, operator.expr_cls):
            raise TypeError(f"Right operand {right} is not of type {operator.expr_cls}")

        self.operator = operator
        self.left = left
        self.right = right

    def accept(self, visitor: "NodeVisitor[T]") -> T:
        return visitor.visit_binary_op(self.left.accept(visitor), self.right.accept(visitor), self.operator)

    def __repr__(self):
        return f"BinaryOp({self.left} {self.operator} {self.right})"


class LessThan(BinaryOp, BoolExpr):
    def __init__(self, left: ExprNode, right: ExprNode):
        super().__init__(BinaryOperator.LESS_THAN, left, right)


class GreaterThan(BinaryOp, BoolExpr):
    def __init__(self, left: ExprNode, right: ExprNode):
        super().__init__(BinaryOperator.GREATER_THAN, left, right)


class Equal(BinaryOp, BoolExpr):
    def __init__(self, left: ExprNode, right: ExprNode):
        super().__init__(BinaryOperator.EQUAL, left, right)


class NotEqual(BinaryOp, BoolExpr):
    def __init__(self, left: ExprNode, right: ExprNode):
        super().__init__(BinaryOperator.NOT_EQUAL, left, right)


class And(BinaryOp, BoolExpr):
    def __init__(self, left: ExprNode, right: ExprNode):
        super().__init__(BinaryOperator.AND, left, right)


class Or(BinaryOp, BoolExpr):
    def __init__(self, left: ExprNode, right: ExprNode):
        super().__init__(BinaryOperator.OR, left, right)
