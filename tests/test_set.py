"""Tests for Set enum."""

from pd2_filter_generator.set import Set


def test_member_exists():
    assert Set.CIVERBS_VESTMENTS is not None


def test_metadata_level():
    assert isinstance(Set.CIVERBS_VESTMENTS.level, int)
