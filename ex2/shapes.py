#################################################################
# FILE : shapes.py
# WRITER :ofir  , ofirm57 , 205660731
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: shape calculate
#################################################################

import math

# function that define how the area of each shape calculate

def circle_area():
    radios = float(input())
    return math.pi*radios**2

def rectangle_area():
    side_1 = float(input())
    side_2 = float(input())
    return side_1 * side_2

def triangle_area():
    triangle_side = float(input())
    return ((3 ** 0.5) / 4) * (triangle_side ** 2)


def shape_area():
    """function that ask the user what shape area he want to
           calculated and what the Measurements of the shape"""

    the_shape = int(input('Choose shape '
                          '(1=circle, 2=rectangle, 3=triangle): '))

    if the_shape < 1 or the_shape > 3:
        return None

    if the_shape == 1:
        return circle_area()

    elif the_shape == 2:
        return rectangle_area()

    elif the_shape == 3:
        return triangle_area()

