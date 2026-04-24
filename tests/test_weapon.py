"""Tests that Weapon enum members are usable in filter expressions."""

from pd2_filter_generator.expression import And, BoolRef, ExprMixin, Not, Or
from pd2_filter_generator.weapon import Weapon


def test_member_is_expr_mixin():
    assert isinstance(Weapon.AXE, ExprMixin)


def test_member_value_code():
    assert Weapon.AXE.value.code == "axe"


def test_invert():
    assert isinstance(~Weapon.AXE, Not)


def test_and_with_bool_literal():
    assert isinstance(Weapon.AXE & BoolRef("ETH"), And)


def test_or_two_members():
    assert isinstance(Weapon.AXE | Weapon.SHORT_SWORD, Or)


def test_chained_or():
    assert isinstance(Weapon.AXE | Weapon.SHORT_SWORD | Weapon.MACE, Or)


def test_combined_with_invert():
    assert isinstance(Weapon.AXE & ~BoolRef("ETH"), And)
