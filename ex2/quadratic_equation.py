#################################################################
# FILE : quadratic_equation.py
# WRITER :ofir  , ofirm57 , 205660731
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: Calculate a quadratic equation
#################################################################

import math

def quadratic_equation(a, b, c):
    """function that takes coefficients of a square equation
    And derives the result of the equation using the root and discriminant
     formula"""
    delta = (b ** 2 - 4 * a * c)

    if delta > 0:
        ans_1 = (-b + math.sqrt(delta)) * (1 / 2 * a)
        ans_2 = (-b - math.sqrt(delta)) * (1 / 2 * a)
        return ans_1, ans_2

    elif delta == 0:
        ans_1 = (-b + math.sqrt(delta)) * (1 / 2 * a)
        return ans_1

    else:
        return None, None


def quadratic_equation_user_input():

    """function that asks the user for three variables and puts them into
        a function (quadratic_equation)And so a solution is
               extracted using the user's input """

    user_in = (input("Insert coefficients a, b, and c: "))
    user_in = user_in.split()

    Solutions = quadratic_equation(float(user_in[0]), float(user_in[1]),
                                   float(user_in[2]))

    if int(user_in[0]) == 0:
        print('The parameter \'a\' may not equal 0')

    elif Solutions != (None, None) and type(Solutions) == tuple:
        print('The equation has 2 solutions: {0} and {1}'
              .format(Solutions[0], Solutions[1]))
    
    elif type(Solutions) == float:
        print('The equation has 1 solution: {}'.format(Solutions))

    elif Solutions == (None, None):
        print('The equation has no solutions')
