import pytest

from seven_segment_display import Digit


@pytest.fixture
def digit():
    return Digit()


@pytest.mark.parametrize("number, components", [
    (0, [" _ ", "| |", "|_|"]),
    (1, ["   ", "  |", "  |"]),
    (2, [" _ ", " _|", "|_ "]),
    (3, [" _ ", " _|", " _|"]),
    (4, ["   ", "|_|", "  |"]),
    (5, [" _ ", "|_ ", " _|"]),
    (6, [" _ ", "|_ ", "|_|"]),
    (7, [" _ ", "  |", "  |"]),
    (8, [" _ ", "|_|", "|_|"]),
    (9, [" _ ", "|_|", "  |"])
])
def test_digit_components(number, components, digit):
    assert digit.digit_components[number] == components


def test_display_single_digit_zero(digit):
    zero = " _ \n| |\n|_|"
    assert digit.display_digit(0) == zero


def test_display_single_digit_seven(digit):
    seven = " _ \n  |\n  |"
    assert digit.display_digit(7) == seven
