def digit(number):
    number_dictionary = {
        0: [" _ ", "| |", "|_|"],
        1: ["   ", "  |", "  |"],
        2: [" _ ", " _|", "|_ "],
        3: [" _ ", " _|", " _|"],
        4: ["   ", "|_|", "  |"],
        5: [" _ ", "|_ ", " _|"],
        6: [" _ ", "|_ ", "|_|"],
        7: [" _ ", "  |", "  |"],
        8: [" _ ", "|_|", "|_|"],
        9: [" _ ", "|_|", "  |"]
    }
    return number_dictionary[number]


def display_digit(number):
    digit_components = digit(number)
    seperator = "\n"
    return seperator.join(digit_components)
