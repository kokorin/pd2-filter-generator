"""Tests for UniqueItem enum."""

import pd2_filter_generator.unique_item as UniqueItem  # noqa: N812


def test_member_exists():
    assert UniqueItem.THE_GNASHER is not None


def test_metadata_code_is_code_literal():
    assert isinstance(UniqueItem.THE_GNASHER.value, str)


def test_metadata_lvl():
    assert isinstance(UniqueItem.THE_GNASHER.lvl, int)


def test_metadata_lvl_req():
    assert isinstance(UniqueItem.THE_GNASHER.lvl_req, int)


def test_metadata_ladder():
    assert isinstance(UniqueItem.THE_GNASHER.ladder, bool)
