#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER :ofir  , ofirm57 , 205660731
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: calculate mathematical
#################################################################

def calculate_mathematical_expression(number1, number2, operator):

    """ function that receives two numbers and one
        Of the four mathematical operations {'+', '-', '*', '/'}
            returns the result of the calculation"""

    if operator == '+':
        return number1 + number2

    elif operator == '-':
        return number1 - number2

    elif operator == '*':
        return number1 * number2

    elif operator == '/':
        if number2 == 0:
            return None
        return number1 / number2

    elif operator is not ['+', '-', '*', '/']:
        return None


def calculate_from_string(string):
    """String-absorbing function translates it into mathematical exercise
     and returns a solution using
      the calculate_mathematical_expression function"""

    y = string.split()

    return calculate_mathematical_expression(float(y[0]), float(y[2]), y[1])
