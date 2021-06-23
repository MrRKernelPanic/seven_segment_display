import pytest

from seven_segment_display import digit, display_digit


@pytest.mark.parametrize("number, components", [
    (0, [' _ ', '| |', '|_|']),
    (1, ['   ', '  |', '  |']),
    (2, [' _ ', ' _|', '|_ ']),
    (3, [' _ ', ' _|', ' _|']),
    (4, ['   ', '|_|', '  |']),
    (5, [' _ ', '|_ ', ' _|']),
    (6, [' _ ', '|_ ', '|_|']),
    (7, [' _ ', '  |', '  |']),
    (8, [' _ ', '|_|', '|_|']),
    (9, [' _ ', '|_|', '  |'])
])
def test_digit_components(number, components):
    assert digit(number) == components


def test_display_single_digit_zero():
    zero = " _ \n| |\n|_|"
    assert display_digit(0) == zero
