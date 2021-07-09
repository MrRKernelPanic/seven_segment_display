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
        self.middle_text = ""
        self.bottom_line = ""
        self.middle_line = ""
        self.middle_top = ""
        self.bottom_top = ""

    def _calculate_top_line(self, width, digit):
        self.top_line += self.digit_components[int(digit)][0][0]
        self.top_line += width * self.digit_components[int(digit)][0][1]
        self.top_line += self.digit_components[int(digit)][0][2]

    def _calculate_middle_line(self, width, digit):
        line = []
        line.append(self.digit_components[int(digit)][1][0])
        line.append(width*self.digit_components[int(digit)][1][1])
        line.append(self.digit_components[int(digit)][1][2])
        seperator = ""
        self.middle_line += seperator.join(line)

    def _calculate_bottom_line(self, width, digit):
        self.bottom_line += self.digit_components[int(digit)][2][0]
        self.bottom_line += width*self.digit_components[int(digit)][2][1]
        self.bottom_line += self.digit_components[int(digit)][2][2]

    def height_padding(self, string_to_pad, height):
        padding = ""
        for i in range(1, height):
            padding += string_to_pad + "\n"
        padding = padding.replace("_", " ")
        return padding

    def display_scaled_number(self, number, width=1, height=1):
        for digit in str(number):
            self._calculate_top_line(width, digit)
            self._calculate_middle_line(width, digit)
            self._calculate_bottom_line(width, digit)

        self.middle_top = self.height_padding(self.middle_line, height)
        self.bottom_top = self.height_padding(self.bottom_line, height)

        fullstring = ""
        fullstring += self.top_line + "\n" + self.middle_top
        fullstring += self.middle_line + "\n"
        fullstring += self.bottom_top + self.bottom_line
        return fullstring
