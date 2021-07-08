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

    def display_scaled_number(self, number, width=1, height=1):
        top_line = ""
        middle_line = []
        bottom_line = ""

        top_line += self.digit_components[int(number)][0][0]
        top_line += width*self.digit_components[int(number)][0][1]
        top_line += self.digit_components[int(number)][0][2]

        line = []
        line.append(self.digit_components[int(number)][1][0])
        line.append(width*self.digit_components[int(number)][1][1])
        line.append(self.digit_components[int(number)][1][2])
        line.append("\n")
        seperator = ""
        middle_line.append(seperator.join(line))

        extra_middle = []
        for i in range(1, height):
            extra_middle.append(self.digit_components[int(number)][1][0])
            extra_middle.append(width*" ")
            extra_middle.append(self.digit_components[int(number)][1][2])
            extra_middle.append("\n")
            seperator = ""
            middle_line.insert(0, seperator.join(extra_middle))
            middle_line.append(seperator.join(extra_middle))

        seperator = ""
        middle_text = seperator.join(middle_line)

        bottom_line += self.digit_components[int(number)][2][0]
        bottom_line += width*self.digit_components[int(number)][2][1]
        bottom_line += self.digit_components[int(number)][2][2]

        return top_line + "\n" + middle_text + bottom_line
