class Digit:

    def __init__(self):
        self.digit_components = {
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

    def display_digit(self, number):
        seperator = "\n"
        return seperator.join(self.digit_components[number])
