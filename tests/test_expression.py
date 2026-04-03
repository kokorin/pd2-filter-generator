"""Tests for expression tree."""
import pytest

from pd2_filter_generator.expression import (
    And,
    Between,
    BinaryOp,
    BinaryOperator,
    Equal,
    GreaterThan,
    LessThan,
    Literal,
    Node,
    NodeVisitor,
    Not,
    NotEqual,
    Or,
)

A = Literal("A")
B = Literal("B")
C = Literal("C")
X = Literal("x")
Y = Literal("y")
Z = Literal("z")


class ToDictVisitor(NodeVisitor[dict]):
    """Visitor that converts expression tree to dict for testing."""

    def visit_literal(self, value: str) -> dict:
        return {"type": "Literal", "value": value}

    def visit_not(self, value: dict) -> dict:
        return {"type": "NOT", "operand": value}

    def visit_binary_op(self, left: dict, right: dict, operator: BinaryOperator) -> dict:
        return {"type": operator.name, "left": left, "right": right}

    def visit_between(self, operand: dict, less_than: dict, greater_than: dict) -> dict:
        return {"type": "BETWEEN", "operand": operand, "less_than": less_than, "greater_than": greater_than}


def to_dict(node: Node) -> dict:
    return node.accept(ToDictVisitor())


class TestNot:
    def test_not(self):
        result = ~A
        assert isinstance(result, Not)
        assert to_dict(result) == {
            "type": "NOT",
            "operand": {"type": "Literal", "value": "A"},
        }

    def test_not_not(self):
        result = ~~A
        assert isinstance(result, Not)
        assert to_dict(result) == {
            "type": "NOT",
            "operand": {
                "type": "NOT",
                "operand": {"type": "Literal", "value": "A"},
            }
        }

    def test_not_compound(self):
        """~(A & B) negates the entire AND expression"""
        result = ~(A & B)
        assert isinstance(result, Not)
        assert to_dict(result) == {
            "type": "NOT",
            "operand": {
                "type": "AND",
                "left": {"type": "Literal", "value": "A"},
                "right": {"type": "Literal", "value": "B"},
            }
        }

    def test_not_or(self):
        """~(A | B) negates the entire OR expression"""
        result = ~(A | B)
        assert to_dict(result) == {
            "type": "NOT",
            "operand": {
                "type": "OR",
                "left": {"type": "Literal", "value": "A"},
                "right": {"type": "Literal", "value": "B"},
            }
        }

class TestBinaryOperators:
    def test_and_operator(self):
        result = A & B
        assert type(result) is And
        assert to_dict(result) == {
            "type": "AND",
            "left": {"type": "Literal", "value": "A"},
            "right": {"type": "Literal", "value": "B"},
        }

    def test_or_operator(self):
        result = A | B
        assert isinstance(result, Or)
        assert to_dict(result) == {
            "type": "OR",
            "left": {"type": "Literal", "value": "A"},
            "right": {"type": "Literal", "value": "B"},
        }

    def test_chained_and(self):
        result = A & B & C
        assert to_dict(result) == {
            "type": "AND",
            "left": {
                "type": "AND",
                "left": {"type": "Literal", "value": "A"},
                "right": {"type": "Literal", "value": "B"},
            },
            "right": {"type": "Literal", "value": "C"},
        }

    def test_precedence_and_over_or(self):
        result = A | B & C
        assert to_dict(result) == {
            "type": "OR",
            "left": {"type": "Literal", "value": "A"},
            "right": {
                "type": "AND",
                "left": {"type": "Literal", "value": "B"},
                "right": {"type": "Literal", "value": "C"},
            },
        }

    def test_chained_or(self):
        """A | B | C is left-to-right: (A | B) | C"""
        result = A | B | C
        assert to_dict(result) == {
            "type": "OR",
            "left": {
                "type": "OR",
                "left": {"type": "Literal", "value": "A"},
                "right": {"type": "Literal", "value": "B"},
            },
            "right": {"type": "Literal", "value": "C"},
        }

    def test_less_than_operator(self):
        result = X < Y
        assert isinstance(result, LessThan)
        assert to_dict(result) == {
            "type": "LESS_THAN",
            "left": {"type": "Literal", "value": "x"},
            "right": {"type": "Literal", "value": "y"},
        }

    def test_greater_than_operator(self):
        result = X > Y
        assert isinstance(result, GreaterThan)
        assert to_dict(result) == {
            "type": "GREATER_THAN",
            "left": {"type": "Literal", "value": "x"},
            "right": {"type": "Literal", "value": "y"},
        }

    def test_equals_operator(self):
        result = X == Y
        assert isinstance(result, Equal)
        assert to_dict(result) == {
            "type": "EQUAL",
            "left": {"type": "Literal", "value": "x"},
            "right": {"type": "Literal", "value": "y"},
        }

    def test_not_equals_operator(self):
        result = X != Y
        assert isinstance(result, NotEqual)
        assert to_dict(result) == {
            "type": "NOT_EQUAL",
            "left": {"type": "Literal", "value": "x"},
            "right": {"type": "Literal", "value": "y"},
        }


class TestBetween:
    def test_between_direct(self):
        result = Between(Y, X, Z)
        assert to_dict(result) == {
            "type": "BETWEEN",
            "operand": {"type": "Literal", "value": "y"},
            "less_than": {"type": "Literal", "value": "x"},
            "greater_than": {"type": "Literal", "value": "z"},
        }

    def test_chained_less_than(self):
        """X < Y < Z creates Between(Y, X, Z)"""
        result = X < Y < Z
        assert isinstance(result, Between)
        assert to_dict(result) == {
            "type": "BETWEEN",
            "operand": {"type": "Literal", "value": "y"},
            "less_than": {"type": "Literal", "value": "x"},
            "greater_than": {"type": "Literal", "value": "z"},
        }

    def test_chained_greater_than(self):
        """X > Y > Z creates Between(Y, Z, X)"""
        result = X > Y > Z
        assert isinstance(result, Between)
        assert to_dict(result) == {
            "type": "BETWEEN",
            "operand": {"type": "Literal", "value": "y"},
            "less_than": {"type": "Literal", "value": "z"},
            "greater_than": {"type": "Literal", "value": "x"},
        }

    def test_between_with_and(self):
        """A & X < Y < Z - between combined with AND"""
        result = A & X < Y < Z
        assert to_dict(result) == {
            "type": "AND",
            "left": {"type": "Literal", "value": "A"},
            "right": {
                "type": "BETWEEN",
                "operand": {"type": "Literal", "value": "y"},
                "less_than": {"type": "Literal", "value": "x"},
                "greater_than": {"type": "Literal", "value": "z"},
            },
        }


class TestCombinedExpression:
    def test_full_expression(self):
        result = A | B & X < Y
        assert to_dict(result) == {
            "type": "OR",
            "left": {"type": "Literal", "value": "A"},
            "right": {
                "type": "AND",
                "left": {"type": "Literal", "value": "B"},
                "right": {
                    "type": "LESS_THAN",
                    "left": {"type": "Literal", "value": "x"},
                    "right": {"type": "Literal", "value": "y"},
                },
            },
        }

    def test_not_with_comparison(self):
        """~A & X > Y"""
        result = ~A & X > Y
        assert to_dict(result) == {
            "type": "AND",
            "left": {
                "type": "NOT",
                "operand": {"type": "Literal", "value": "A"},
            },
            "right": {
                "type": "GREATER_THAN",
                "left": {"type": "Literal", "value": "x"},
                "right": {"type": "Literal", "value": "y"},
            },
        }

    def test_multiple_comparisons_with_or(self):
        """X < Y | A > B"""
        result = X < Y | A > B
        assert to_dict(result) == {
            "type": "OR",
            "left": {
                "type": "LESS_THAN",
                "left": {"type": "Literal", "value": "x"},
                "right": {"type": "Literal", "value": "y"},
            },
            "right": {
                "type": "GREATER_THAN",
                "left": {"type": "Literal", "value": "A"},
                "right": {"type": "Literal", "value": "B"},
            },
        }

    def test_complex_nested(self):
        """(A | B) & (X == Y)"""
        result = (A | B) & (X == Y)
        assert to_dict(result) == {
            "type": "AND",
            "left": {
                "type": "OR",
                "left": {"type": "Literal", "value": "A"},
                "right": {"type": "Literal", "value": "B"},
            },
            "right": {
                "type": "EQUAL",
                "left": {"type": "Literal", "value": "x"},
                "right": {"type": "Literal", "value": "y"},
            },
        }


class TestPrecedenceValues:
    def test_comparison_precedence_highest(self):
        assert BinaryOperator.LESS_THAN.precedence < BinaryOperator.AND.precedence

    def test_and_precedence_over_or(self):
        assert BinaryOperator.AND.precedence < BinaryOperator.OR.precedence

    def test_all_comparisons_equal_precedence(self):
        assert BinaryOperator.LESS_THAN.precedence == BinaryOperator.GREATER_THAN.precedence
        assert BinaryOperator.LESS_THAN.precedence == BinaryOperator.EQUAL.precedence
        assert BinaryOperator.LESS_THAN.precedence == BinaryOperator.NOT_EQUAL.precedence


class TestAbstractClasses:
    def test_node_cannot_be_instantiated(self):
        with pytest.raises(TypeError):
            Node()

    def test_binary_op_cannot_be_instantiated(self):
        with pytest.raises(TypeError):
            BinaryOp(A, B, BinaryOperator.AND)