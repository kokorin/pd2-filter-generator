"""Tests for expression tree."""

import pytest

from pd2_filter_generator.expression import (
    And,
    BinaryOp,
    BinaryOperator,
    BoolRef,
    Equal,
    GreaterThan,
    IntLit,
    ExprLeaf,
    LessThan,
    ExprNode,
    NodeVisitor,
    Not,
    NotEqual,
    Or,
)

# Boolean refs - PD2 flags / item-type predicates
NMAG = BoolRef("NMAG")
RARE = BoolRef("RARE")
BOOTS = BoolRef("BOOTS")

# Integer refs - PD2 numeric stats
SOCKETS = IntLit("SOCKETS")
CLVL = IntLit("CLVL")
GOLD = IntLit("GOLD")
ONE = IntLit("1")
TWO = IntLit("2")
TEN = IntLit("10")


class ToDictVisitor(NodeVisitor[dict]):
    """Visitor that converts expression tree to dict for testing."""

    def visit_literal(self, value: str) -> dict:
        return {"type": "Literal", "value": value}

    def visit_not(self, value: dict) -> dict:
        return {"type": "NOT", "operand": value}

    def visit_binary_op(self, left: dict, right: dict, operator: BinaryOperator) -> dict:
        return {"type": operator.name, "left": left, "right": right}


def to_dict(node: ExprNode) -> dict:
    return node.accept(ToDictVisitor())


# =============================================================================
# Test Hierarchy: Tests organized by type hierarchy
# =============================================================================


class TestNode:
    """Tests for Node base class."""

    def test_node_cannot_be_instantiated(self):
        """Node is abstract and cannot be instantiated directly."""
        with pytest.raises(TypeError):
            ExprNode()

    def test_node_bool_raises_error_in_if(self):
        """Cannot use nodes in if statements."""
        with pytest.raises(TypeError, match=r"Cannot use.*in boolean context"):
            bool(SOCKETS < TEN)

    def test_node_bool_raises_error_with_and_keyword(self):
        """Cannot use 'and' keyword (must use & operator)."""
        comparison = SOCKETS < TEN
        with pytest.raises(TypeError, match=r"Cannot use.*in boolean context"):
            comparison and NMAG  # noqa: B018

    def test_node_bool_raises_error_with_or_keyword(self):
        """Cannot use 'or' keyword (must use | operator)."""
        with pytest.raises(TypeError, match=r"Cannot use.*in boolean context"):
            NMAG or RARE  # noqa: B018

    def test_node_bool_raises_error_with_not_keyword(self):
        """Cannot use 'not' keyword (must use ~ operator)."""
        with pytest.raises(TypeError, match=r"Cannot use.*in boolean context"):
            not NMAG  # noqa: B018

    def test_node_bool_raises_error_with_chained_comparison(self):
        """Chained comparisons raise TypeError."""
        with pytest.raises(TypeError, match=r"Cannot use.*in boolean context"):
            ONE < SOCKETS < TWO  # noqa: B015


class TestBoolExpr:
    """Tests for BoolExpr - supports ~, &, | operators."""

    def test_invert_creates_not(self):
        """~NMAG creates Not node."""
        result = ~NMAG
        assert isinstance(result, Not)
        assert to_dict(result) == {
            "type": "NOT",
            "operand": {"type": "Literal", "value": "NMAG"},
        }

    def test_double_invert(self):
        """~~NMAG creates nested Not nodes."""
        result = ~~NMAG
        assert isinstance(result, Not)
        assert to_dict(result) == {
            "type": "NOT",
            "operand": {
                "type": "NOT",
                "operand": {"type": "Literal", "value": "NMAG"},
            },
        }

    def test_invert_compound_expression(self):
        """~(NMAG & RARE) negates the entire AND expression."""
        result = ~(NMAG & RARE)
        assert isinstance(result, Not)
        assert to_dict(result) == {
            "type": "NOT",
            "operand": {
                "type": "AND",
                "left": {"type": "Literal", "value": "NMAG"},
                "right": {"type": "Literal", "value": "RARE"},
            },
        }

    def test_invert_or_expression(self):
        """~(NMAG | RARE) negates the entire OR expression."""
        result = ~(NMAG | RARE)
        assert to_dict(result) == {
            "type": "NOT",
            "operand": {
                "type": "OR",
                "left": {"type": "Literal", "value": "NMAG"},
                "right": {"type": "Literal", "value": "RARE"},
            },
        }

    def test_and_creates_and_node(self):
        """NMAG & BOOTS creates And node."""
        result = NMAG & BOOTS
        assert type(result) is And
        assert to_dict(result) == {
            "type": "AND",
            "left": {"type": "Literal", "value": "NMAG"},
            "right": {"type": "Literal", "value": "BOOTS"},
        }

    def test_or_creates_or_node(self):
        """NMAG | RARE creates Or node."""
        result = NMAG | RARE
        assert isinstance(result, Or)
        assert to_dict(result) == {
            "type": "OR",
            "left": {"type": "Literal", "value": "NMAG"},
            "right": {"type": "Literal", "value": "RARE"},
        }

    def test_chained_and(self):
        """NMAG & RARE & BOOTS chains left-to-right."""
        result = NMAG & RARE & BOOTS
        assert to_dict(result) == {
            "type": "AND",
            "left": {
                "type": "AND",
                "left": {"type": "Literal", "value": "NMAG"},
                "right": {"type": "Literal", "value": "RARE"},
            },
            "right": {"type": "Literal", "value": "BOOTS"},
        }

    def test_chained_or(self):
        """NMAG | RARE | BOOTS chains left-to-right."""
        result = NMAG | RARE | BOOTS
        assert to_dict(result) == {
            "type": "OR",
            "left": {
                "type": "OR",
                "left": {"type": "Literal", "value": "NMAG"},
                "right": {"type": "Literal", "value": "RARE"},
            },
            "right": {"type": "Literal", "value": "BOOTS"},
        }

    def test_and_precedence_over_or(self):
        """NMAG | RARE & BOOTS: & has higher precedence."""
        result = NMAG | RARE & BOOTS
        assert to_dict(result) == {
            "type": "OR",
            "left": {"type": "Literal", "value": "NMAG"},
            "right": {
                "type": "AND",
                "left": {"type": "Literal", "value": "RARE"},
                "right": {"type": "Literal", "value": "BOOTS"},
            },
        }

    def test_and_validates_right_operand_is_bool(self):
        """AND requires both operands to be BoolExpr."""
        with pytest.raises(TypeError, match="BoolExpr"):
            NMAG & SOCKETS

    def test_or_validates_right_operand_is_bool(self):
        """OR requires both operands to be BoolExpr."""
        with pytest.raises(TypeError, match="BoolExpr"):
            NMAG | CLVL

    def test_comparison_results_are_boolean(self):
        """Comparison results are BoolExpr and can use &, |, ~."""
        comparison = SOCKETS < TEN

        result = NMAG & comparison
        assert isinstance(result, And)

        negated = ~comparison
        assert isinstance(negated, Not)


class TestIntExpr:
    """Tests for IntExpr - supports ==, !=, <, > operators."""

    def test_equal_operator(self):
        """== creates Equal node."""
        result = SOCKETS == CLVL
        assert isinstance(result, Equal)
        assert to_dict(result) == {
            "type": "EQUAL",
            "left": {"type": "Literal", "value": "SOCKETS"},
            "right": {"type": "Literal", "value": "CLVL"},
        }

    def test_not_equal_operator(self):
        """!= creates NotEqual node."""
        result = SOCKETS != GOLD
        assert isinstance(result, NotEqual)
        assert to_dict(result) == {
            "type": "NOT_EQUAL",
            "left": {"type": "Literal", "value": "SOCKETS"},
            "right": {"type": "Literal", "value": "GOLD"},
        }

    def test_less_than_operator(self):
        """< creates LessThan node."""
        result = SOCKETS < CLVL
        assert isinstance(result, LessThan)
        assert to_dict(result) == {
            "type": "LESS_THAN",
            "left": {"type": "Literal", "value": "SOCKETS"},
            "right": {"type": "Literal", "value": "CLVL"},
        }

    def test_greater_than_operator(self):
        """> creates GreaterThan node."""
        result = CLVL > GOLD
        assert isinstance(result, GreaterThan)
        assert to_dict(result) == {
            "type": "GREATER_THAN",
            "left": {"type": "Literal", "value": "CLVL"},
            "right": {"type": "Literal", "value": "GOLD"},
        }

    def test_equal_validates_right_operand_is_int(self):
        """== requires both operands to be IntExpr."""
        with pytest.raises(TypeError, match="IntExpr"):
            SOCKETS == NMAG  # noqa: B015

    def test_not_equal_validates_right_operand_is_int(self):
        """!= requires both operands to be IntExpr."""
        with pytest.raises(TypeError, match="IntExpr"):
            SOCKETS != NMAG  # noqa: B015

    def test_less_than_validates_right_operand_is_int(self):
        """< requires both operands to be IntExpr."""
        with pytest.raises(TypeError, match="IntExpr"):
            SOCKETS < NMAG  # noqa: B015

    def test_greater_than_validates_right_operand_is_int(self):
        """> requires both operands to be IntExpr."""
        with pytest.raises(TypeError, match="IntExpr"):
            SOCKETS > NMAG  # noqa: B015

    def test_comparison_results_are_boolean(self):
        """Comparison results are BoolExpr."""
        result = SOCKETS < TEN

        combined = NMAG & result
        assert isinstance(combined, And)

        negated = ~result
        assert isinstance(negated, Not)

    def test_equality_results_are_boolean(self):
        """Equality results are BoolExpr."""
        result = SOCKETS == ONE
        assert isinstance(result, Equal)

        combined = NMAG & result
        assert isinstance(combined, And)


class TestLeaf:
    """Tests for leaf node types and their capabilities."""

    def test_leaf_base_class_cannot_be_instantiated(self):
        """Leaf is abstract."""
        with pytest.raises(TypeError):
            ExprLeaf("x")

    # =========================================================================
    # BoolRef: supports &, |, ~ only
    # =========================================================================

    def test_bool_ref_supports_and_operator(self):
        result = NMAG & BOOTS
        assert isinstance(result, And)

    def test_bool_ref_supports_or_operator(self):
        result = NMAG | RARE
        assert isinstance(result, Or)

    def test_bool_ref_supports_invert_operator(self):
        result = ~NMAG
        assert isinstance(result, Not)

    def test_bool_ref_blocks_less_than(self):
        with pytest.raises(TypeError):
            NMAG < RARE  # noqa: B015

    def test_bool_ref_blocks_greater_than(self):
        with pytest.raises(TypeError):
            NMAG > RARE  # noqa: B015

    def test_bool_ref_blocks_equal(self):
        with pytest.raises(TypeError):
            NMAG == RARE  # noqa: B015

    def test_bool_ref_blocks_not_equal(self):
        with pytest.raises(TypeError):
            NMAG != RARE  # noqa: B015

    # =========================================================================
    # IntLit: supports <, >, ==, != only (NOT ~, &, |)
    # =========================================================================

    def test_int_lit_supports_less_than_operator(self):
        result = SOCKETS < TWO
        assert isinstance(result, LessThan)

    def test_int_lit_supports_greater_than_operator(self):
        result = SOCKETS > ONE
        assert isinstance(result, GreaterThan)

    def test_int_lit_supports_equal_operator(self):
        result = SOCKETS == ONE
        assert isinstance(result, Equal)

    def test_int_lit_supports_not_equal_operator(self):
        result = SOCKETS != TWO
        assert isinstance(result, NotEqual)

    def test_int_lit_blocks_invert(self):
        with pytest.raises(TypeError):
            ~SOCKETS  # noqa: B018

    def test_int_lit_blocks_and_operator(self):
        with pytest.raises(TypeError):
            SOCKETS & CLVL

    def test_int_lit_blocks_or_operator(self):
        with pytest.raises(TypeError):
            SOCKETS | CLVL


class TestBinaryOp:
    """Tests for BinaryOp base class."""

    def test_binary_op_cannot_be_instantiated(self):
        """BinaryOp is abstract."""
        with pytest.raises(TypeError):
            BinaryOp(NMAG, RARE, BinaryOperator.AND)

    def test_visitor_pattern_for_binary_ops(self):
        """All binary operations work with visitor pattern."""
        expr = NMAG & (SOCKETS < TEN)
        result = to_dict(expr)
        assert result["type"] == "AND"
        assert result["left"]["type"] == "Literal"
        assert result["right"]["type"] == "LESS_THAN"


class TestOperatorPrecedence:
    """Tests for operator precedence values."""

    def test_comparison_precedence_highest(self):
        """Comparisons have highest precedence (lowest value)."""
        assert BinaryOperator.LESS_THAN.precedence < BinaryOperator.AND.precedence

    def test_and_precedence_over_or(self):
        """AND has higher precedence than OR."""
        assert BinaryOperator.AND.precedence < BinaryOperator.OR.precedence

    def test_all_comparisons_equal_precedence(self):
        """All comparison operators have equal precedence."""
        assert BinaryOperator.LESS_THAN.precedence == BinaryOperator.GREATER_THAN.precedence
        assert BinaryOperator.LESS_THAN.precedence == BinaryOperator.EQUAL.precedence
        assert BinaryOperator.LESS_THAN.precedence == BinaryOperator.NOT_EQUAL.precedence


class TestComplexExpressions:
    """Tests for real-world PD2 filter patterns."""

    def test_full_expression(self):
        """NMAG | RARE & (SOCKETS < CLVL) - needs parentheses due to precedence"""
        result = NMAG | RARE & (SOCKETS < CLVL)
        assert to_dict(result) == {
            "type": "OR",
            "left": {"type": "Literal", "value": "NMAG"},
            "right": {
                "type": "AND",
                "left": {"type": "Literal", "value": "RARE"},
                "right": {
                    "type": "LESS_THAN",
                    "left": {"type": "Literal", "value": "SOCKETS"},
                    "right": {"type": "Literal", "value": "CLVL"},
                },
            },
        }

    def test_not_with_comparison(self):
        """~NMAG & (CLVL > GOLD) - needs parentheses"""
        result = ~NMAG & (CLVL > GOLD)
        assert to_dict(result) == {
            "type": "AND",
            "left": {
                "type": "NOT",
                "operand": {"type": "Literal", "value": "NMAG"},
            },
            "right": {
                "type": "GREATER_THAN",
                "left": {"type": "Literal", "value": "CLVL"},
                "right": {"type": "Literal", "value": "GOLD"},
            },
        }

    def test_multiple_comparisons_with_or(self):
        """(SOCKETS < CLVL) | (GOLD > CLVL) - both need parentheses"""
        result = (SOCKETS < CLVL) | (GOLD > CLVL)
        assert to_dict(result) == {
            "type": "OR",
            "left": {
                "type": "LESS_THAN",
                "left": {"type": "Literal", "value": "SOCKETS"},
                "right": {"type": "Literal", "value": "CLVL"},
            },
            "right": {
                "type": "GREATER_THAN",
                "left": {"type": "Literal", "value": "GOLD"},
                "right": {"type": "Literal", "value": "CLVL"},
            },
        }

    def test_complex_nested(self):
        """(NMAG | RARE) & (SOCKETS == CLVL)"""
        result = (NMAG | RARE) & (SOCKETS == CLVL)
        assert to_dict(result) == {
            "type": "AND",
            "left": {
                "type": "OR",
                "left": {"type": "Literal", "value": "NMAG"},
                "right": {"type": "Literal", "value": "RARE"},
            },
            "right": {
                "type": "EQUAL",
                "left": {"type": "Literal", "value": "SOCKETS"},
                "right": {"type": "Literal", "value": "CLVL"},
            },
        }
