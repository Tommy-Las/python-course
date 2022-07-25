# def ifcolor(r, g, b):
#     colors_dict = {"red": (1, 0, 0), "green": (0, 1, 0), "blue": (0, 0, 1), "cyan": (
#         0, 1, 1), "magenta": (1, 0, 1), "yellow": (1, 1, 0), "black": (0, 0, 0), "white": (1, 1, 1)}
#     for key in colors_dict:
#         if(r == colors_dict[key][0] and r == colors_dict[key][1] and r == colors_dict[key][2]):
#             return key
#     return -1

class Color(object):
    def __init__(self, r, g, b):
        # coerce values into required range by saturating
        # dictionary that holds predefined colors and their rgb values, will be used in a later function
        self.colors_dict = {"Red": (1, 0, 0), "Green": (0, 1, 0), "Blue": (0, 0, 1), "Cyan": (
            0, 1, 1), "Magenta": (1, 0, 1), "Yellow": (1, 1, 0), "Black": (0, 0, 0), "White": (1, 1, 1)}
        # if rgb values are greater than 1, will be set to 1. if rgb values are less than 0, will be set to 0
        if r < 0:
            r = 0
        if r > 1:
            r = 1
        if g < 0:
            g = 0
        if g > 1:
            g = 1
        if b < 0:
            b = 0
        if b > 1:
            b = 1
        # rgb values for self color
        self.red = float(r)
        self.green = float(g)
        self.blue = float(b)

    def __add__(self, x):
        # enter code here
        red = self.red + x.red
        if red > 1:
            red = 1
        green = self.green + x.green
        if green > 1:
            green = 1
        blue = self.blue + x.blue
        if blue > 1:
            blue = 1
        # checks if it is a predefined color or not
        answer = self.if_color(red, green, blue)
        # if it is not a predefined color, it will print rgb values
        if answer == -1:
            return f"({red:.1f}, {green:.1f}, {blue:.1f})"
        else:
            return answer

    def __sub__(self, x):
        # enter code here
        red = self.red - x.red
        if red < 0:
            red = 0
        green = self.green - x.green
        if green < 0:
            green = 0
        blue = self.blue - x.blue
        if blue < 0:
            blue = 0
        # checks if it is a predefined color or not
        answer = self.if_color(red, green, blue)
        # if it is not a predefined color, it will print rgb values
        if answer == -1:
            return f"({red:.1f}, {green:.1f}, {blue:.1f})"
        else:  # is a predefined color
            return answer

    def __str__(self):
        color = self.if_color(self.red, self.green, self.blue)
        if color == -1:
            return f"({self.red:.1f}, {self.green:.1f}, {self.blue:.1f})"
        else:
            return color

    def __repr__(self):
        return self.__str__()

    # function that traverses through dictionary and checks if the rgb values given are from a color
    def if_color(self, r, g, b):
        for key in self.colors_dict:
            if(r == self.colors_dict[key][0] and g == self.colors_dict[key][1] and b == self.colors_dict[key][2]):
                return key
        return -1


def display_instructions():
    print("\nThe purpose of this program is to ask the user to enter to colors\n\
either by three integers or its name, and compute the sum and the difference of both colors\n\n\
Valid color names: red, green, blue, cyan, magenta, yellow, black and white\n")

# it makes the input cleaner, if it is numbers or a given name


def create_color(color, colors_dict):

    if(color.isalpha()):
        color = color.strip().lower()
        for key in colors_dict:
            if key == color:
                return Color(colors_dict[color][0],
                             colors_dict[color][1], colors_dict[color][2])
        return -1
    else:
        color = color.strip('() ')
        color = color.replace(" ", "")
        color_list = color.split(',')
        return Color(float(color_list[0]),
                     float(color_list[1]), float(color_list[2]))


def main():
    colors_dict = {"red": (1, 0, 0), "green": (0, 1, 0), "blue": (0, 0, 1), "cyan": (
        0, 1, 1), "magenta": (1, 0, 1), "yellow": (1, 1, 0), "black": (0, 0, 0), "white": (1, 1, 1)}
    display_instructions()
    input1 = input(
        "Enter the name or rgb values (r, g, b) of the first color: ")
    color1 = create_color(input1, colors_dict)
    input2 = input(
        "Enter the name or rgb values (r, g, b) of the second color: ")
    color2 = create_color(input2, colors_dict)

    if(color1 == -1 or color2 == -1):
        print("ERROR: VALUES NOT VALID")
    else:
        print(f"Color1 = {color1}")
        print(f"Color2 = {color2}")
        print(f"Color1 + Color2 = {color1 + color2}")
        print(f"Color2 - Color1 = {color1 - color2}")


main()
