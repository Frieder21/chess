class colour:
    def ansi_text_coloring_hex_colour(self, text, colour):
        colour = [int(colour[1:3], 16), int(colour[3:5], 16), int(colour[5:7], 16)]
        return f"\033[38;2;{colour[0]};{colour[1]};{colour[2]}m{text}\033[00m"

    def ansi_background_coloring_hex_colour(self, text, colour):
        colour = [int(colour[1:3], 16), int(colour[3:5], 16), int(colour[5:7], 16)]
        return f"\033[48;2;{colour[0]};{colour[1]};{colour[2]}m{text}\033[00m"

    def ansi_text_and_background_coloring_hex_colour(self, text, text_colour, background_colour):
        return self.ansi_background_coloring_hex_colour(self.ansi_text_coloring_hex_colour(text, text_colour), background_colour)

    def ansi_text_coloring(self, text, colour):
        return self.ansi_text_coloring_hex_colour(text, self.colour_scheme[colour])
    def ansi_background_coloring(self, text, colour):
        return self.ansi_background_coloring_hex_colour(text, self.colour_scheme[colour])

    def ansi_text_and_background_coloring(self, text, text_colour, background_colour):
        return self.ansi_background_coloring(self.ansi_text_coloring(text, text_colour), background_colour)

    def __init__(self, colour_scheme=None):
        self.colour_scheme = colour_scheme
        if self.colour_scheme is None:
            self.colour_scheme = {
                "green": "#00FF00",
                "yellow": "#FFFF00",
                "red": "#FF0000",
                "blue": "#0000FF",
                "magenta": "#FF00FF",
                "cyan": "#00FFFF",
                "white": "#FFFFFF",
                "black": "#000000",
                "grey": "#808080"
            }

def clear_to_start(text):
    import sys
    lines = text.split('\n')  # separate lines
    lines = lines[::-1]  # reverse list
    n_lines = len(lines)  # number of lines
    for i, line in enumerate(lines):  # iterate through lines from last to first
        sys.stdout.write('\r')  # move to beginning of line
        sys.stdout.write(' ' * len(line))  # replace text with spaces (thus overwriting it)
        if i < n_lines - 1:  # not first line of text
            sys.stdout.write('\x1b[1A')  # move up one line
    sys.stdout.write('\r')  # move to beginning of line again

class letter_and_int:
    def int_to_caps_letter(self, number):
        return chr(number + 65)

    def caps_letter_to_int(self, letter):
        return ord(letter) - 65

    def int_to_lower_letter(self, number):
        return chr(number + 97)

    def lower_letter_to_int(self, letter):
        return ord(letter) - 97