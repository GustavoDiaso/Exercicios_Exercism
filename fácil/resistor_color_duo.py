"""
Instructions
If you want to build something using a Raspberry Pi, you'll probably use resistors. For this exercise, you need to know
two things about them:

Each resistor has a resistance value.
Resistors are small - so small in fact that if you printed the resistance value on them, it would be hard to read.
To get around this problem, manufacturers print color-coded bands onto the resistors to denote their resistance values.
Each band has a position and a numeric value.

The first 2 bands of a resistor have a simple encoding scheme: each color maps to a single number. For example, if they
printed a brown band (value 1) followed by a green band (value 5), it would translate to the number 15.

In this exercise you are going to create a helpful program so that you don't have to remember the values of the bands.
The program will take color names as input and output a two digit number, even if the input is more than two colors!

The band colors are encoded as follows:

black: 0
brown: 1
red: 2
orange: 3
yellow: 4
green: 5
blue: 6
violet: 7
grey: 8
white: 9
From the example above: brown-green should return 15, and brown-green-violet should return 15 too, ignoring the third
color.
"""


def resistor_color_duo(input_colors: str) -> int:
    color_code = {
        "black": '0',
        "brown": '1',
        "red": '2',
        "orange": '3',
        "yellow": '4',
        "green": '5',
        "blue": '6',
        "violet": '7',
        "grey": '8',
        "white": '9',
    }

    input_colors = input_colors.strip().lower()
    colors_list = input_colors.split('-')

    if len(colors_list) == 2:
        try:
            resistence_value = f'{color_code[colors_list[0]]}{color_code[colors_list[1]]}'
            return int(resistence_value)
        except KeyError as k_error:
            raise Exception(f"The color {k_error} does not exist")

    else:
        raise Exception("The program only accepts 2 color-band values")




print(resistor_color_duo('blue-green'))




