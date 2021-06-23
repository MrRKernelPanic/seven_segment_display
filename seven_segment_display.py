def digit(number):
    if number == 0:
        return [" _ ", "| |", "|_|"]
    if number == 1:
        return ["   ", "  |", "  |"]


def display_digit(number):
    digit_components = digit(number)
    seperator = "\n"
    return seperator.join(digit_components)
