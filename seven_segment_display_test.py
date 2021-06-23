import pytest

from seven_segment_display import digit, display_digit


def test_digit():
    assert digit(0) == [" _ ", "| |", "|_|"]


def test_display_single_digit_zero():
    zero = " _ \n| |\n|_|"
    assert display_digit(0) == zero
