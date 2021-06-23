import pytest

from seven_segment_display import digit, display_digit


@pytest.mark.parametrize("number, components", [
    (0, [' _ ', '| |', '|_|']),
    (1, ['   ', '  |', '  |']),
])
def test_digit_components(number, components):
    assert digit(number) == components


def test_display_single_digit_zero():
    zero = " _ \n| |\n|_|"
    assert display_digit(0) == zero
