"""Tests for SetItem enum."""

from pd2_filter_generator.set import Set
from pd2_filter_generator.set_item import SetItem


def test_member_exists():
    assert SetItem.CIVERBS_WARD is not None


def test_member_value_is_string():
    assert isinstance(SetItem.CIVERBS_WARD.value, str)


def test_metadata_set_reference():
    assert SetItem.CIVERBS_WARD.set is Set.CIVERBS_VESTMENTS


def test_metadata_lvl():
    assert isinstance(SetItem.CIVERBS_WARD.lvl, int)


def test_metadata_lvl_req():
    assert isinstance(SetItem.CIVERBS_WARD.lvl_req, int)
