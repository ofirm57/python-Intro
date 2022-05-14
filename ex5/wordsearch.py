#################################################################
# FILE : wordsearch.py
# WRITER :ofir  , ofirm57 , 205660731
# EXERCISE : intro2cs2 ex5 2020
# DESCRIPTION: The function captures 3 arguments (words, the matrix,
# and directions) and emits an argument of the words that appear in the matrix
# according to the directions of the directions.
#################################################################

import sys
from collections import Counter
from copy import deepcopy
import os

ERROR_LENGTH = 'error: The number of parameters is different from 4'
ERROR_FILE = 'error: File {} not found'
ERROR_DIRECTION = 'error: Input directions is incorrect'
DIRECTION = 'udlrwxyz'


def direction_check(direction_arg):
    """
    :param direction_arg: The letters that direct search directions in
    the matrix
    :return:True if we have problem in the input of the direction if not False
    """
    for let in direction_arg:
        if let not in DIRECTION:
            return True
    else:
        return False


def check_input_args(args):
    """
    :param args: list of 4 args not including args[0]
    :return: None if  all the checks is ok, if one of the check is invalid
    the function return one of the error string by for each case
    """
    if len(args) != 4:
        return ERROR_LENGTH
    elif not os.path.isfile(args[0]):
        return ERROR_FILE.format('word_file')
    elif not os.path.isfile(args[1]):
        return ERROR_FILE.format('matrix_file')
    elif direction_check(args[3]):
        return ERROR_DIRECTION
    else:
        return None


def read_wordlist_file(filename):
    """
    function that open the word list and return list of word
    :param filename: file whit words that speared by \n
    :return: list of words
    """
    with open(filename) as word:
        word_file_lst = word.read()
        word_file_lst = word_file_lst.split("\n")[:-1]
    return word_file_lst


def read_matrix_file(filename):
    """
    :param filename: file whit matrix of letters
    :return: list of list for each row in the matrix
    """
    with open(filename, 'r') as mat_file:
        the_matrix = []
        for sting in mat_file:
            line = sting.split('\n')
            line.pop()
            tmp_line = line[0].split(',')
            the_matrix.append(tmp_line)
        return the_matrix


def write_output_file(results, output_filename):
    """
    :param results: list of tupels (the found word , 1)
    :param output_filename: the file that the program write to
    """
    with open(output_filename, 'w') as my_file:
        for tup in results:
            if tup != results[-1]:
                reversing_to_string = (tup[0] + ',' + str(tup[1]) + '\n')
                my_file.write(reversing_to_string)
            if tup == results[-1]:
                reversing_to_string = (tup[0] + ',' + str(tup[1]))
                my_file.write(reversing_to_string)


def the_finder(word_file_lst, the_matrix):
    """
    :param word_file_lst: the lis with the word
    :param the_matrix: list of lists ,
    :return: list of all the words that appear in the matrix
    """
    results = []
    for word in word_file_lst:
        for row in the_matrix:
            row_join = "".join(row)
            if word in row_join:
                matches = count_check(row_join, word)
                results.extend([word for i in range(matches)])
    return results


def count_check(row_str, word_check):
    """
    :param row_str: string from row in the matrix
    :param word_check: string of word
    :return:The number of word impressions in the string of the row
    """
    word_len = len(word_check)
    matches_number = 0
    for start_i in range(len(row_str)):
        if row_str[start_i:start_i + word_len] == word_check:
            matches_number += 1
    return matches_number


def reversing_line_to_row(the_matrix):
    """
    :param the_matrix: list of lists ,the matrix
    :return:  Matrix with row change in column
    """
    rearranged_lst = []
    change_mat_line_row = deepcopy(the_matrix)
    matrix_length = len(change_mat_line_row)
    if not change_mat_line_row:
        return change_mat_line_row
    internal_length = len(change_mat_line_row[0])
    for line in range(internal_length):
        tmp_lst = []
        for row in range(matrix_length):
            tmp_lst.append(change_mat_line_row[row][line])
            if row == matrix_length - 1:
                rearranged_lst.append(tmp_lst)
    return rearranged_lst


def internal_r_to_left(the_matrix):
    """
    :param the_matrix: list of lists , the matrix
    :return:A list whose organs on the internal list flipped
    """
    if not the_matrix:
        return the_matrix
    reserve_mat = deepcopy(the_matrix)
    for row in range(len(reserve_mat)):
        reserve_mat[row] = reserve_mat[row][::-1]
    return reserve_mat


def reserving_external(the_matrix):
    """
    :param the_matrix: list of lists , the matrix
    :return:List of list which the order of lists is reversed
    """
    mat_reserve = deepcopy(the_matrix)
    mat_reserve = mat_reserve[::-1]
    return mat_reserve


def slant(internal_length, matrix_length, j, row, the_matrix, tmp_list,
          end_lst):
    """Auxiliary function for diagonals in the matrix
    A function that takes variables from the {diagonal_list(the_matrix)}
    function and returns a list
    of diagonals
    """
    while row <= matrix_length or j <= internal_length:
        tmp_list.append(the_matrix[row][j])
        row += 1
        j += 1
        if j == internal_length or row == matrix_length:
            end_lst.append(tmp_list)
            break
    return end_lst


def diagonal_list(the_matrix):
    """
    :param the_matrix: list of list the matrix
    :return: List of list, the diagonals of the matrix
    """
    diagonal_planning = deepcopy(the_matrix)
    if not the_matrix:
        return diagonal_planning
    matrix_length = len(the_matrix)
    internal_length = len(the_matrix[0])
    end_lst = []
    side1_lst = []
    side2_lst = []
    for row in range(matrix_length):
        j = 0
        tmp_list = []
        side1_lst = slant(internal_length, matrix_length, j, row,
                          diagonal_planning, tmp_list, end_lst)
    row = 0
    end_lst = []
    for j in range(1, internal_length):
        tmp_list = []
        side2_lst = slant(internal_length, matrix_length, j, row,
                          diagonal_planning, tmp_list, end_lst)
    diagonal = side1_lst + side2_lst
    return diagonal


def direction_y(word_file_lst, the_matrix):
    """
    :param word_file_lst:list of words
    :param the_matrix: list of list, the matrix
    :return:List of words found in direction y
    """
    the_cross_y = diagonal_list(the_matrix)
    y = the_finder(word_file_lst, the_cross_y)
    return y


def direction_z(word_file_lst, the_matrix):
    """
    :param word_file_lst:list of words
    :param the_matrix:list of list, the matrix
    :return:List of words found in direction z
    """
    the_matrix = internal_r_to_left(the_matrix)
    the_cross_z = diagonal_list(the_matrix)
    z = the_finder(word_file_lst, the_cross_z)
    return z


def direction_w(word_file_lst, the_matrix):
    """
    :param word_file_lst:list of words
    :param the_matrix:list of list, the matrix
    :return:List of words found in direction w
    """
    rev_w = reserving_external(the_matrix)
    w = direction_y(word_file_lst, rev_w)
    return w


def direction_x(word_file_lst, the_matrix):
    """

    :param word_file_lst:list of words
    :param the_matrix:list of list, the matrix
    :return:List of words found in direction x
    """
    the_cross_x_matt = reserving_external(the_matrix)
    x = direction_z(word_file_lst, the_cross_x_matt)
    return x


def direction_r(word_file_lst, the_matrix):
    """
    :param word_file_lst:list of words
    :param the_matrix:list of list, the matrix
    :return:List of words found in direction r
    """
    right = the_finder(word_file_lst, the_matrix)
    return right


def direction_l(word_file_lst, the_matrix):
    """
    :param word_file_lst:list of words
    :param the_matrix:list of list, the matrix
    :return:List of words found in direction left
    """
    reserve_mat = internal_r_to_left(the_matrix)
    left = the_finder(word_file_lst, reserve_mat)
    return left


def direction_u(word_file_lst, the_matrix):
    """
    :param word_file_lst:list of words
    :param the_matrix:list of list, the matrix
    :return:List of words found in direction u
    """
    rearranged_lst = reversing_line_to_row(the_matrix)
    mat_for_u = internal_r_to_left(rearranged_lst)
    up = the_finder(word_file_lst, mat_for_u)
    return up


def direction_d(word_file_lst, the_matrix):
    """
   :param word_file_lst:list of words
    :param the_matrix:list of list, the matrix
    :return:List of words found in direction d
    """
    rearranged_lst = reversing_line_to_row(the_matrix)
    down = the_finder(word_file_lst, rearranged_lst)
    return down


def find_words_in_matrix(word_file_lst, the_matrix, directions):
    """
    :param word_file_lst:list of words
    :param the_matrix:list of list, the matrix
    :param directions: the string with the direction
    :return: list of tuple with th word and number 1
    """
    tmp_result = []
    if 'u' in directions:
        tmp_result.append(direction_u(word_file_lst, the_matrix))
    if 'd' in directions:
        tmp_result.append(direction_d(word_file_lst, the_matrix))
    if 'r' in directions:
        tmp_result.append(direction_r(word_file_lst, the_matrix))
    if 'l' in directions:
        tmp_result.append(direction_l(word_file_lst, the_matrix))
    if 'w' in directions:
        tmp_result.append(direction_w(word_file_lst, the_matrix))
    if 'x' in directions:
        tmp_result.append(direction_x(word_file_lst, the_matrix))
    if 'y' in directions:
        tmp_result.append(direction_y(word_file_lst, the_matrix))
    if 'z' in directions:
        tmp_result.append(direction_z(word_file_lst, the_matrix))
    tmp_result = sum(tmp_result, [])
    res_dict = Counter(tmp_result)
    tup_results = [(key, value) for key, value in res_dict.items()]
    return tup_results


def main(argv):
    """The main function that regulates the operations
    :param argv: arguments from the program
    :return:if the checks isnt ok  print erorr
    """
    args = [argv[1], argv[2], argv[3], argv[4]]
    the_check = check_input_args(args)
    if the_check is None:
        words_lst = read_wordlist_file(argv[1])
        matrix = read_matrix_file(argv[2])
        the_result = find_words_in_matrix(words_lst, matrix, argv[4])
        write_output_file(the_result, argv[3])
    else:
        print(the_check)


if __name__ == '__main__':
    main(sys.argv)
