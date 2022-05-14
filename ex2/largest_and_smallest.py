#################################################################
# FILE : largest_and_smallest.py
# WRITER :ofir  , ofirm57 , 205660731
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: max and min
#################################################################


def largest_and_smallest(number_1, number_2, number_3):

    """function that calculate max and min between three numbers"""

    if number_1 >= number_2 >= number_3 or number_1 >= number_3 >= number_2:
        if number_2 >= number_3:
            return number_1, number_3

        else:
            return number_1, number_2

    if number_2 >= number_1 >= number_3 or number_2 >= number_3 >= number_1:
        if number_1 >= number_3:
            return number_2, number_3

        else:
            return number_2, number_1

    if number_3 >= number_1 >= number_2 or number_3 >= number_2 >= number_1:
        if number_1 >= number_2:
            return number_3, number_2

        else:
            return number_3, number_1


def check_largest_and_smallest():
    """A function that checks the validity of a function largest_
        and_smallest by running equations and returning a boolean value"""

    if largest_and_smallest(17, 1, 6) == (17, 1):

        if largest_and_smallest(1, 17, 6) == (17, 1):

            if largest_and_smallest(1, 1, 2) == (2, 1):

                if largest_and_smallest(-1, 5**0, -1/0.1) == (1, -10):

                    if largest_and_smallest(0.5, 3.4, 1/2) == (3.4, 1/2):
                        return True

                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
