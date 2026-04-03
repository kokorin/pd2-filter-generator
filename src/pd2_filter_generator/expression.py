"""Expression tree for PD2 filter conditions."""
from abc import ABC, abstractproperty, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import TypeVar, Generic

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

    @abstractmethod
    def visit_between(self, operand: T, less_than: T, greater_than: T) -> T:
        pass


class Node(ABC):
    """Base class for expression tree nodes."""

    @abstractmethod
    def accept(self, visitor: NodeVisitor[T]) -> T:
        pass

    def __invert__(self):
        return Not(self)

    def __and__(self, other: "Node"):
        return And(self, other)

    def __or__(self, other: "Node"):
        return Or(self, other)

    def __lt__(self, other: "Node"):
        return LessThan(self, other)

    def __gt__(self, other: "Node"):
        return GreaterThan(self, other)

    def __ne__(self, other: "Node"):
        return NotEqual(self, other)

    def __eq__(self, other: "Node"):
        return Equal(self, other)

    @abstractmethod
    def __repr__(self):
        pass


class Literal(Node):
    """Leaf node holding a value."""

    def __init__(self, value: str):
        self.value = value

    def accept(self, visitor: NodeVisitor[T]) -> T:
        return visitor.visit_literal(self.value)

    def __repr__(self):
        return f"Literal({self.value})"


class Not(Node):
    def __init__(self, operand: Node):
        self.operand = operand

    def accept(self, visitor: NodeVisitor[T]) -> T:
        operand = self.operand.accept(visitor)
        return visitor.visit_not(operand)

    def __repr__(self):
        return f"Not({self.operand})"


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


class BinaryOp(Node, ABC):

    def __init__(self, left: Node, right: Node, operator: BinaryOperator):
        if type(self) is BinaryOp:
            # we need at least 1 abstract method for ABC to block direct instantiation
            raise TypeError("Cannot instantiate BinaryOp directly")

        self.left = left
        self.right = right
        self.operator = operator

    def accept(self, visitor: NodeVisitor[T]) -> T:
        left = self.left.accept(visitor)
        right = self.right.accept(visitor)
        return visitor.visit_binary_op(left, right, self.operator)

    def __repr__(self):
        return f"BinaryOp({self.left} {self.operator} {self.right})"


class LessThan(BinaryOp):
    def __init__(self, left: Node, right: Node):
        super().__init__(left, right, BinaryOperator.LESS_THAN)


class GreaterThan(BinaryOp):
    def __init__(self, left: Node, right: Node):
        super().__init__(left, right, BinaryOperator.GREATER_THAN)


class Equal(BinaryOp):
    def __init__(self, left: Node, right: Node):
        super().__init__(left, right, BinaryOperator.EQUAL)

class NotEqual(BinaryOp):
    def __init__(self, left: Node, right: Node):
        super().__init__(left, right, BinaryOperator.NOT_EQUAL)


class And(BinaryOp):
    def __init__(self, left: Node, right: Node):
        super().__init__(left, right, BinaryOperator.AND)


class Or(BinaryOp):
    def __init__(self, left: Node, right: Node):
        super().__init__(left, right, BinaryOperator.OR)


class Between(Node):
    def __init__(self, operand: Node, less_than: Node, greater_than: Node):
        self.operand = operand
        self.less_than = less_than
        self.greater_than = greater_than

    def accept(self, visitor: NodeVisitor[T]) -> T:
        operand = self.operand.accept(visitor)
        less_than = self.less_than.accept(visitor)
        greater_than = self.greater_than.accept(visitor)
        return visitor.visit_between(operand, less_than, greater_than)
