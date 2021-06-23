import pytest

from seven_segment_display import digit


def test_digit():
    assert digit(0) == [" _ ", "| |", "|_|"]
