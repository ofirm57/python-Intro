#################################################################
# FILE : math_print.py
# WRITER :ofir  , ofirm57 , 205660731
# EXERCISE : intro2cs2 ex1 2020
# DESCRIPTION: A simple program that doing math .
#################################################################

import math


def golden_ratio():
    """A function that prints the value of the constant of golden ratio"""
    print(0.5 * (1 + math.sqrt(5)))


def six_squared():
    """A function that prints the value of 6**2"""
    print(6 ** 2)


def hypotenuse():
    """A function that prints the value of a hypotenuse in a right triangle
    whose sides are "a" , "b" """
    (a, b) = 5, 12
    print(math.sqrt(a ** 2 + b ** 2))


def pi():
    """ A function that prints the value of pi"""
    print(math.pi)


def e():
    """A function that prints the value of e"""
    print(math.e)


def squares_area():
    """ A function that prints all the possibilities of a square space
    depending on the square side (1-10)"""
    print(1 ** 2, 2 ** 2, 3 ** 2, 4 ** 2, 5 ** 2, 6 ** 2, 7 ** 2, 8 ** 2,
          9 ** 2, 10 ** 2)


if __name__ == "__main__":
    """the main function"""
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    squares_area()
