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


class BoolExpr(ExprNode, ABC):
    """Nodes representing boolean expressions. Support ~, &, | operators."""

    def __invert__(self) -> "BoolExpr":
        return Not(self)

    def __and__(self, other: "BoolExpr") -> "BoolExpr":
        return And(self, other)

    def __or__(self, other: "BoolExpr") -> "BoolExpr":
        return Or(self, other)


class IntExpr(ExprNode, ABC):
    """Nodes supporting ordering operators (==, !=, <, >)."""

    def __hash__(self):
        msg = f"Cannot hash {type(self).__name__}"
        raise TypeError(msg)

    def __eq__(self, other: "IntExpr") -> BoolExpr:  # type: ignore[override]
        return Equal(self, other)

    def __ne__(self, other: "IntExpr") -> BoolExpr:  # type: ignore[override]
        return NotEqual(self, other)

    def __lt__(self, other: "IntExpr") -> BoolExpr:
        return LessThan(self, other)

    def __gt__(self, other: "IntExpr") -> BoolExpr:
        return GreaterThan(self, other)


class ExprLeaf(ExprNode, ABC):
    """Leaf node holding a value."""

    def __init__(self, value: str):
        self.value = value

    def accept(self, visitor: "NodeVisitor[T]") -> T:
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
        self.operand = operand

    def accept(self, visitor: "NodeVisitor[T]") -> T:
        return visitor.visit_not(self.operand.accept(visitor))

    def __repr__(self):
        return f"Not({self.operand})"


class BinaryOp(ExprNode, ABC):
    def __init__(self, left: ExprNode, right: ExprNode):
        self.left = left
        self.right = right

    @property
    @abstractmethod
    def operator(self) -> BinaryOperator:
        pass

    def accept(self, visitor: "NodeVisitor[T]") -> T:
        return visitor.visit_binary_op(self.left.accept(visitor), self.right.accept(visitor), self.operator)

    def __repr__(self):
        return f"BinaryOp({self.left} {self.operator} {self.right})"


class LessThan(BinaryOp, BoolExpr):
    @property
    def operator(self) -> BinaryOperator:
        return BinaryOperator.LESS_THAN


class GreaterThan(BinaryOp, BoolExpr):
    @property
    def operator(self) -> BinaryOperator:
        return BinaryOperator.GREATER_THAN


class Equal(BinaryOp, BoolExpr):
    @property
    def operator(self) -> BinaryOperator:
        return BinaryOperator.EQUAL


class NotEqual(BinaryOp, BoolExpr):
    @property
    def operator(self) -> BinaryOperator:
        return BinaryOperator.NOT_EQUAL


class And(BinaryOp, BoolExpr):
    @property
    def operator(self) -> BinaryOperator:
        return BinaryOperator.AND


class Or(BinaryOp, BoolExpr):
    @property
    def operator(self) -> BinaryOperator:
        return BinaryOperator.OR
