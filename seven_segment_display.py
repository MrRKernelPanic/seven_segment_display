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

        self.top_line = ""
        self.middle_top = ""
        self.middle_line = ""
        self.bottom_top = ""
        self.bottom_line = ""
        self.middle_text = ""

    def display_scaled_number(self, number, width=1, height=1):
        self.calculate_width(number, width)
        self.calculate_height(height)
        fullstring = self.combining_to_final_string()
        return fullstring

    def calculate_width(self, number, width):
        for digit in str(number):
            self.top_line += self._calculate_line(digit, width, 0)
            self.middle_line += self._calculate_line(digit, width, 1)
            self.bottom_line += self._calculate_line(digit, width, 2)

    def _calculate_line(self, digit, width, row):
        digit = int(digit)
        line = ""
        line += self.digit_components[digit][row][0]
        line += width * self.digit_components[digit][row][1]
        line += self.digit_components[digit][row][2]
        return line

    def calculate_height(self, height):
        self.middle_top = self.height_padding(self.middle_line, height)
        self.bottom_top = self.height_padding(self.bottom_line, height)

    def height_padding(self, string_to_pad, height):
        padding = ""
        for i in range(1, height):
            padding += string_to_pad + "\n"
        padding = padding.replace("_", " ")
        return padding

    def combining_to_final_string(self):
        fullstring = ""
        fullstring += self.top_line + "\n" + self.middle_top
        fullstring += self.middle_line + "\n"
        fullstring += self.bottom_top + self.bottom_line
        return fullstring
