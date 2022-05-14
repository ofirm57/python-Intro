#################################################################
# FILE : ex7.py
# WRITER :ofir  , ofirm57 , 205660731
# EXERCISE : intro2cs2 ex7 2020
#################################################################


def print_to_n(n):
    """
    function that receives an integer (n)
    and return end returns all numbers from n to 1"""
    if n < 1:
        return
    if n > 0:
        print_to_n(n - 1)
        print(n)


def digit_sum(n):
    """A function that receives a number greater than 0 and returns the sum
     of its digits"""
    if n < 10:
        return n
    else:
        return n % 10 + digit_sum(n // 10)


def has_divisor_smaller_than(n, i):
    """Auxiliary function for "is prime"
    Receiving number (n) and  (i = the divider) and return True if prime
    else False"""
    if i == 1:
        return True
    if n % i == 0 and n != 2:
        return False
    else:
        return has_divisor_smaller_than(n, i - 1)


def is_prime(n):
    """function that receive number (n) and return True if the number is
    prime"""
    if n < 2:
        return False
    else:
        return has_divisor_smaller_than(n, int(n ** 0.5 + 1))


def play_hanoi(hanoi, n, src, dst, temp):
    """ function that plays the "Tower of Hanoi" ,Accepts a destination,
    source, and temporary destination,Number of discs to move
    and the game itself (hanoi)"""
    if n <= 0:
        return
    if n == 1:
        hanoi.move(src, dst)
    else:
        play_hanoi(hanoi, n - 1, src, temp, dst)
        play_hanoi(hanoi, 1, src, dst, temp)
        play_hanoi(hanoi, n - 1, temp, dst, src)


def helper_for_sequences_functions(char_list, tmp_string, n, no_repet):
    """Auxiliary function for "print_sequences", and
    "print_no_repetition_sequences" .
    The function receives a character list, a string, a number of combinations
    and the option of not repeating characters
    And takes the combinations out according to variables"""
    if no_repet and len(tmp_string) > 1:
        for i in tmp_string:
            if tmp_string.count(i) > 1:
                return
    if not char_list:
        return
    if n == 0:
        print(tmp_string)
        return
    for i in range(len(char_list)):
        new_tmp_str = tmp_string + char_list[i]
        helper_for_sequences_functions(char_list, new_tmp_str, n - 1, no_repet)


def print_sequences(char_list, n):
    """A function that prints the character list combinations of n length"""
    helper_for_sequences_functions(char_list, "", n, False)


def print_no_repetition_sequences(char_list, n):
    """A function that prints the character list combinations of n length
    with No repetition of character"""
    helper_for_sequences_functions(char_list, '', n, True)


def helper_for_parentheses(n, r, tmp_str, lst):
    """Auxiliary function for 'parentheses' got sring,list number of
     combinations and more number, and return the right combinations"""
    if n == 0 and r == 0:
        lst.append(tmp_str)
        return lst
    if n >= 1:
        new_tmp_str = tmp_str + '('
        helper_for_parentheses(n - 1, r, new_tmp_str, lst)
    if r > n:
        new_tmp_str = tmp_str + ')'
        helper_for_parentheses(n, r - 1, new_tmp_str, lst)
    return lst


def parentheses(n):
    """function that returns list of strings that contains all the forms that
    can by from n times legit parentheses ,use 'helper_for_parentheses' """
    pat_lst = helper_for_parentheses(n, n, "", [])
    return pat_lst


def helper_for_flood_fill(image, start_row, start_line):
    """receive list, start row points and start line points
    And changes the theme to '*' if the image is not blocked by "*" From top
    to bottom and to the sides """
    image[start_row][start_line] = '*'
    if image[start_row][start_line + 1] == '.':  # R
        flood_fill(image, (start_row, start_line + 1))
    if image[start_row][start_line - 1] == '.':  # L
        flood_fill(image, (start_row, start_line - 1))
    if image[start_row - 1][start_line] == '.':  # D
        flood_fill(image, (start_row - 1, start_line))
    if image[start_row + 1][start_line] == '.':  # UP
        flood_fill(image, (start_row + 1, start_line))
    return image


def flood_fill(image, start):
    """receive list and start points (tuple) """
    helper_for_flood_fill(image, start[0], start[1])
