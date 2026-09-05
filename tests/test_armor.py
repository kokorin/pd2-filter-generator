"""Tests that Armor enum members are usable in filter expressions."""

import pd2_filter_generator.armor as Armor  # noqa: N812
from pd2_filter_generator.expression import And, BoolRef, Not, Or


def test_member_is_expr_mixin():
    assert isinstance(Armor.FULL_PLATE_MAIL, BoolRef)


def test_member_value_code():
    assert Armor.FULL_PLATE_MAIL.value == "ful"


def test_invert():
    assert isinstance(~Armor.FULL_PLATE_MAIL, Not)


def test_and_with_bool_literal():
    assert isinstance(Armor.FULL_PLATE_MAIL & BoolRef("ETH"), And)


def test_or_two_members():
    assert isinstance(Armor.CAP | Armor.HELM, Or)


def test_chained_or():
    assert isinstance(Armor.CAP | Armor.HELM | Armor.FULL_HELM, Or)


def test_combined_with_invert():
    assert isinstance(Armor.FULL_PLATE_MAIL & ~BoolRef("ETH"), And)
