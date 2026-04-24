"""Tests for Set enum."""

from pd2_filter_generator.set import Set


def test_member_exists():
    assert Set.CIVERBS_VESTMENTS is not None


def test_member_value_is_string():
    assert isinstance(Set.CIVERBS_VESTMENTS.value, str)


def test_metadata_level():
    assert isinstance(Set.CIVERBS_VESTMENTS.level, int)
