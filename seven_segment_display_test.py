import pytest

from seven_segment_display import SevenSegmentDisplay


@pytest.fixture
def display():
    return SevenSegmentDisplay()


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
def test_digit_components(number, components, display):
    assert display.digit_components[number] == components


def test_display_single_digit_zero(display):
    zero = " _ \n| |\n|_|"
    assert display.display_numbers(0) == zero


def test_display_single_digit_seven(display):
    seven = " _ \n  |\n  |"
    assert display.display_numbers(7) == seven


def test_display_multiple_digits_(display):
    fourtyseven = "    _ \n|_|  |\n  |  |"
    assert display.display_numbers(47) == fourtyseven


def test_horizontally_scaled_digit(display):
    three = " __ \n __|\n __|"
    assert display.display_scaled_number(3, 2) == three


def test_scalable_digit(display):
    three = " __ \n   |\n __|\n   |\n __|"
    assert display.display_scaled_number(3, 2, 2) == three
