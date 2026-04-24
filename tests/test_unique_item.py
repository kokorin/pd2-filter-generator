"""Tests for UniqueItem enum."""

from pd2_filter_generator.unique_item import UniqueItem


def test_member_exists():
    assert UniqueItem.THE_GNASHER is not None


def test_metadata_code_is_code_literal():
    assert isinstance(UniqueItem.THE_GNASHER.code, str)


def test_metadata_lvl():
    assert isinstance(UniqueItem.THE_GNASHER.lvl, int)


def test_metadata_lvl_req():
    assert isinstance(UniqueItem.THE_GNASHER.lvl_req, int)


def test_metadata_ladder():
    assert isinstance(UniqueItem.THE_GNASHER.ladder, bool)
