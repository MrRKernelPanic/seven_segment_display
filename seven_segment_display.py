class SevenSegmentDisplay:

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

    def display_numbers(self, number):
        top_line = ""
        middle_line = ""
        bottom_line = ""

        for digit in str(number):
            top_line += self.digit_components[int(digit)][0]
            middle_line += self.digit_components[int(digit)][1]
            bottom_line += self.digit_components[int(digit)][2]
        return top_line + "\n" + middle_line + "\n" + bottom_line
