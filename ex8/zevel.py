# # # def queensproblem(rows, columns):
# # #     solutions = [[]]
# # #     for row in range(rows):
# # #         solutions = add_one_queen(row, columns, solutions)
# # #     return solutions
# # #

















#################################################################
# FILE : ex8.py
# WRITER :ofir  , ofirm57 , 205660731
# EXERCISE : intro2cs2 ex8 2020
#################################################################
import math

BLACK = 1
WHITE = 0
UNKNOWN = -1


def helper_get_row_variations(row, blocks, tmp_lst, row_lst, index,
                              first_t=True):
    """function that return all the option of row by the block
    :param row: list of row
    :param blocks: listof block
    :param tmp_lst: change list
    :param row_lst: the return list
    :param index: the index
    :param first_t: true if u first time entar the function
    """
    length = len(row)
    if first_t:
        found_common_cases = common_cases(row, blocks)
        if found_common_cases:
            answer = get_intersection_row([row, found_common_cases])
            if not rows_with_unknown_check([answer]):
                return [found_common_cases]
    if sum(blocks) - sum(tmp_lst) > len(row) - len(tmp_lst):
        return
    if tmp_lst.count(BLACK) > sum(blocks):
        return
    if tmp_lst.count(WHITE) > length - sum(blocks):
        return
    if index > 1 and not row_check(tmp_lst, blocks, index, length):
        return
    if len(row_lst) == count_row_variations(length, blocks):
        return row_lst
    if len(tmp_lst) == length:
        if tmp_lst.count(BLACK) != sum(blocks):
            return
        return row_lst.append(tmp_lst)
    if row[index] == UNKNOWN:
        tmp_lst.append(BLACK)
        helper_get_row_variations(row, blocks, tmp_lst[:], row_lst, index + 1,
                                  False)
        tmp_lst[-1] = WHITE
        helper_get_row_variations(row, blocks, tmp_lst[:], row_lst, index + 1,
                                  False)
    else:
        tmp_lst.append(row[index])
        helper_get_row_variations(row, blocks, tmp_lst[:], row_lst, index + 1,
                                  False)
    return row_lst


def common_cases(row, block):
    """
    recive row and block and return common_cases
    """
    row_long = len(row)
    num_of_black = sum(block)
    block_length = len(block)
    lst = []
    if num_of_black + len(block) - 1 == row_long:
        for i, value in enumerate(block):
            lst.extend([BLACK] * value)
            if i != block_length - 1:
                lst.append(WHITE)
        return lst
    if not block: ### zero row
        return lst.extend([WHITE] * row_long)
    if block_length == 1 and num_of_black == row_long:  ## all black
        return lst.extend([BLACK] * row_long)


def row_check(tmp_lst, blocks, index, lenght):  # func 1
    """
    finction that check the row by the blocks, index and  lenght
    """
    counter = 0
    b_num = 0
    for i, v in enumerate(tmp_lst):
        if i != index - 1: # check if first
            if v == BLACK:
                counter += 1
                if tmp_lst[i + 1] == 0:
                    if blocks[b_num] != counter:
                        return False
                    else:
                        counter = 0
                        b_num += 1
        else:
            if v == BLACK:
                counter += 1
                if blocks[b_num] != counter and not i < lenght - 1:
                    return False
    return True


def get_row_variations(row, blocks): #func 1 real
    """function that return option fo row by the blocks information """
    return helper_get_row_variations(row, blocks, [], [], 0, True)


####################################################################^1

def make_list_of_index(rows):
    """function that replicates the list of lists"""
    lenght = len(rows[0])
    option_num = len(rows)
    tmp_lst = []
    list_of_index = []
    for i in range(lenght):  # line
        if i != 0:
            list_of_index.append(tmp_lst)
            tmp_lst = []
        for j in range(option_num):  # row external
            tmp_lst.append(rows[j][i])
    list_of_index.append(tmp_lst)
    return list_of_index


def get_intersection_row(rows):  # func 2
    """ recive list of list (option for one row) and return the option for
    the row
    i choose that this func return only what is 100% right"""

    the_rows = make_list_of_index(rows)
    result = []
    for i in range(len(the_rows)):
        if all(x == the_rows[i][0] for x in the_rows[i]): ###IF ALL THE SAME
            result.append(the_rows[i][0])
            continue
        if 0 in the_rows[i] and (1 or -1) in the_rows[i]:
            result.append(UNKNOWN)
            continue
        result.append(UNKNOWN)

    return result

#########################################################################^2


def solve_easy_nonogram(constraints):  ## main
    """make the firs check and then cotinue to check if it not redey"""
    bord = find_start_bord(constraints)
    return helper_func3(constraints, bord)


def find_start_bord(constraints):
    """
    A function that makes a board according to constraints Length
    """
    line_num = len(constraints[1])
    row_num = len(constraints[0])
    first_bord = []
    for i in range(row_num):
        tmp = []
        tmp.extend([UNKNOWN] * line_num)
        first_bord.append(tmp)
    return first_bord


def helper_func3(constraints, start_bord):
    """
    A function that takes out a resolved or partially resolved board
    With the help of auxiliary functions like first_line_solution and
    find_start_bord
    """
    line_solution = first_line_solution(constraints, start_bord)
    row_solution = first_row_solution(constraints, line_solution)
    if row_solution == line_solution:
        return row_solution
    make_2_check_loops = 2
    while make_2_check_loops:
        tmp_lst = []
        for i in range(len(row_solution)):
            end_com_result = compre_list(row_solution[i], line_solution[i])
            tmp_lst.append(end_com_result)
            if make_2_check_loops == 0:
                return tmp_lst
            if make_2_check_loops == 0:
                break
        row_solution = first_row_solution(constraints, tmp_lst)
        line_solution = first_line_solution(constraints, row_solution)
        if row_solution != line_solution:
            make_2_check_loops = 2
        else:
            make_2_check_loops -= 1

    return row_solution



def first_row_solution(constraints, list_of_rows):
    """A function that sends a line for review"""
    line_number = len(constraints[1])
    check_index = 0
    return check_row_and_line(check_index, constraints, line_number, [],
                              list_of_rows)



def compre_list(row_1, row_2):
    """ compere two list if value1 is -1 and value2 is 1 or 0 the function
    chage value1 to 1 or 0, the function return the number of -1 appeared in
     the valu1 and value2     """
    if row_1 == row_2:
        return row_2
    for i in range(len(row_1)):
        if row_1[i] != row_2[i]:
            if row_1[i] == -1:
                row_1[i] = row_2[i]
            elif row_2[i] == -1:
                continue
            else:
                return # if problem with the check
    return row_1


def first_line_solution(constraints, start_bord):
    """ its make reverse and if there isnt start bord, its make one  """
    rows_number = len(constraints[0])
    check_index = 1
    row_side_sol = make_list_of_index(start_bord)
    new_lines = check_row_and_line(check_index, constraints, rows_number,
                                   [], row_side_sol)
    line_result = make_list_of_index(new_lines)
    return line_result


def check_row_and_line(index, constraints, line_number,tmp_solution,start_row):
    """
    :return: posibale option for bord by check the row
    """
    tmp_result = []
    for i, value in enumerate(constraints[index]):
        if not (bool(value)):
            tmp_solution.append([WHITE] * line_number)
            continue
        if len(value) == 1 and sum(value) == line_number:
            tmp_solution.append([BLACK] * line_number)
            continue
        else:
            if type(start_row[0]) is list:
                tmp_result = get_row_variations(start_row[i], value)
            if not type(start_row[0]) is list:
                tmp_result = get_row_variations([-1] * line_number, value)
            if len(tmp_result) == 1:
                tmp_solution.append(tmp_result[0])
                continue
            if len(tmp_result) > 1:
                the_best_option = get_intersection_row(tmp_result)
                tmp_solution.append(the_best_option)
            else:
                tmp_solution.append([UNKNOWN] * line_number)
    return tmp_solution

#####################################################################^3


def solve_nonogram_helper4(constraints, option, simple_result, num=0,
                           first_enter=True):
    """
   A function that solves a board with the help of possible rows inlay and if
   there are no contradictions the function takes the board out
    """

    global rows_option
    if first_enter:
        simple_result = solve_easy_nonogram(constraints) ### solve easy
        if not rows_with_unknown_check(simple_result):
            return [simple_result]

    if not simple_result:
        return
    # list of the index of rows with -1
    list_of_index = rows_with_unknown_check(simple_result)
    if not list_of_index:
        if option:
            if check_if_results_same(option, simple_result):
                return
        return option.append(simple_result)
    index = list_of_index[num]
    if list_of_index:
        rows_option = get_row_variations(simple_result[index],
                                         constraints[0][index])
    for j in range(len(rows_option)):
        if UNKNOWN in rows_option[j] and rows_option[j][1:] \
                == rows_option[j][:-1]:
            continue
        if rows_option[j] == simple_result[index]:
            continue
        simple_result[index] = rows_option[j]
        # simple_result = check_row_and_line(0, constraints, len(constraints[1])
        #                                    , [], simple_result)

        simple_result = helper_func3(constraints, simple_result)
        solve_nonogram_helper4(constraints, option, simple_result, 0, False)
        if j == len(rows_option) - 1 and index == list_of_index[-1]:
            return
    return option


def check_if_results_same(option, simple_result):
    """ return TRUE if same
     else return false"""
    for i in option:
        if i == simple_result:
            return True
    return False


def rows_with_unknown_check(bord):
    """check if the bord contain -1
    :param bord: the list of list (the bord)
    :return: [] if the bord is full'
     else return list with the row index who contain -1"""
    rows_with_unknown = []
    if not bord:
        return
    for i, row in enumerate(bord):
        if UNKNOWN in row:
            rows_with_unknown.append(i)
    return rows_with_unknown


def solve_nonogram(constraints):  #### func 4
    return solve_nonogram_helper4(constraints, [], [])


#############################################################^4

def count_row_variations(length, blocks):
    num_block = len(blocks)
    the_amount_of_black = sum(blocks)
    k = length - the_amount_of_black - (num_block - 1)
    if k < 0:
        return 0
    n = length - the_amount_of_black + 1
    return int(binom_n_k(n, k))


def binom_n_k(n, k):
    f = math.factorial
    return f(n) / f(k) / f(n-k)

#################################################################^5
AAA = [[1],[2],[2],[2],[1],[1]],[[2],[2],[2],[3]]
T =[[ [1], [1] ], [ [1], [1] ]]
print(solve_nonogram(T))
solve_nonogram([[ [1], [1] ], [ [1], [1] ]])

COUNT = 0 ###########################  לזכור למחוק !!!!!!!!
COUNT4 = 0
BLACK = 1
WHITE = 0
UNKNOWN = -1

import math
#################################### יעילות לפי אורך שורה

def helper_get_row_variations(row, blocks, tmp_lst, row_lst, index, first_t=True, black_index=list):  # func 1 helper
    global COUNT
    length = len(row)
    #
    if first_t:
        found_common_cases = common_cases(row, blocks)
        if found_common_cases:
            answer = get_intersection_row([row, found_common_cases])
            if not rows_with_unknown_check([answer]):
                return [found_common_cases]
    # if black_index and len(blocks) == 1:
    #     if index in black_index and tmp_lst[index - 1] == WHITE:
    #         return
    if sum(blocks) - sum(tmp_lst) > len(row) - len(tmp_lst):
        return
    if tmp_lst.count(BLACK) > sum(blocks):
        return
    if tmp_lst.count(WHITE) > length - sum(blocks):
        return
        pass
    if index > 1 and not row_check(tmp_lst, blocks, index, length):
        return
    if len(row_lst) == count_row_variations(length, blocks):
        return row_lst
    if len(tmp_lst) == length:
        if tmp_lst.count(BLACK) != sum(blocks):
            return
        return row_lst.append(tmp_lst)
    COUNT += 1
    if row[index] == UNKNOWN:
        tmp_lst.append(BLACK)
        helper_get_row_variations(row, blocks, tmp_lst[:], row_lst, index + 1, False, black_index)
        tmp_lst[-1] = WHITE
        helper_get_row_variations(row, blocks, tmp_lst[:], row_lst, index + 1, False, black_index)
    else:
        tmp_lst.append(row[index])
        helper_get_row_variations(row, blocks, tmp_lst[:], row_lst, index + 1, False, black_index)
    return row_lst


def common_cases(row, block):
    row_long = len(row)
    num_of_black = sum(block)
    block_length = len(block)
    lst = []
    if num_of_black + len(block) - 1 == row_long:   ################################# make the only row thets posibaol
        for i, value in enumerate(block):
            lst.extend([BLACK] * value)
            if i != block_length - 1:
                lst.append(WHITE)
        return lst
    if not block: ### zero row
        return lst.extend([WHITE] * row_long)
    if block_length == 1 and num_of_black == row_long:  ## all black
        return lst.extend([BLACK] * row_long)



def mast_be_bleck(row, block):
    """ func that return list of index that mast be black"""
    row_long = len(row)
    num_of_black = sum(block)
    block_length = len(block)
    if block_length == 1 and row_long/2 < num_of_black: ####const black
        start_indx = row_long - num_of_black
        end_indx = num_of_black - 1
        # add_amount = num_of_black - start_indx
        # print(start_indx)
        # print(end_indx)
        return list(range(start_indx, end_indx+1))

        # for i in range(row_long):
        #     if i == start_i_black:
        #         lst.extend([BLACK] * add_amount)
        #         i += add_amount
        #     else:
        #         lst.append(UNKNOWN)
        # return lst



def row_check(tmp_lst, blocks, index, lenght):  # func 1
    """
    :return True if the checks is ok
    :param tmp_lst:
    :param blocks:
    :return:
    """
    counter = 0
    b_num = 0
    block_check = blocks[b_num]
    for i, v in enumerate(tmp_lst):
        if i != index - 1: # check if first?
            if v == BLACK:
                counter += 1
                if tmp_lst[i + 1] == 0:
                    if blocks[b_num] != counter:
                        return False
                    else:
                        counter = 0
                        b_num += 1
        else:
            if v == BLACK:
                counter += 1
                if blocks[b_num] != counter and not i < lenght - 1:  ##
                    return False
    return True


def get_row_variations(row, blocks): #func 1 real
    black_index = mast_be_bleck(row, blocks)
    x = helper_get_row_variations(row, blocks, [], [], 0, True, black_index)
    return x


####################################################################^1

def make_list_of_index(rows):
    lenght = len(rows[0])
    n = len(rows)
    tmp_lst = []
    list_of_index = []
    for i in range(lenght):  # line
        if i != 0:
            list_of_index.append(tmp_lst)
            tmp_lst = []
        for j in range(n):  # row external
            tmp_lst.append(rows[j][i])
    list_of_index.append(tmp_lst)
    return list_of_index


def get_intersection_row(rows):  # func 2
    """ recive list of list (option for one row) and return the option for
    the row
    זה עובר על אינדקסים של השורות
    i choose that this func return only what is 100% right"""

    the_rows = make_list_of_index(rows)
    result = []
    for i in range(len(the_rows)):
        if all(x == the_rows[i][0] for x in the_rows[i]): ###IF ALL THE SAME
            result.append(the_rows[i][0])
            continue
        if 0 in the_rows[i] and (1 or -1) in the_rows[i]:
            result.append(UNKNOWN)
            continue
        result.append(UNKNOWN)

    return result


#########################################################################^2

############################################################################

def solve_easy_nonogram(constraints):  ## main
    """make the firs check and then cotinue to check if it not redey"""
    # empty_list = []
    bord = find_start_bord(constraints)
    return helper_func3(constraints, bord)


def find_start_bord(constraints):
    """
    make mat
    :param constraints:
    :return:
    """
    line_num = len(constraints[1])
    row_num = len(constraints[0])
    first_bord = []
    for i in range(row_num):
        tmp = []
        tmp.extend([UNKNOWN] * line_num)
        first_bord.append(tmp)
    return first_bord


def helper_func3(constraints, start_bord):

    line_solution = first_line_solution(constraints, start_bord)
    row_solution = first_row_solution(constraints, line_solution)
    if row_solution == line_solution:
        return row_solution
    make_2_check_loops = 2
    while make_2_check_loops:

        tmp_lst = []
        for i in range(len(row_solution)):
            end_com_result = compre_list(row_solution[i], line_solution[i])
            tmp_lst.append(end_com_result)
        row_solution = first_row_solution(constraints, tmp_lst)
        line_solution = first_line_solution(constraints, row_solution)
        if row_solution != line_solution:
            make_2_check_loops = 2
        else:
            make_2_check_loops -= 1
            if make_2_check_loops == 0:
                break

    return line_solution



def first_row_solution(constraints, list_of_rows):
    line_number = len(constraints[1])
    check_index = 0
    return check_row_and_line(check_index, constraints, line_number, [],
                              list_of_rows)



def compre_list(row_1, row_2):
    """ compere two list if value1 is -1 and value2 is 1 or 0 the function
    chage value1 to 1 or 0, the function return the number of -1 appeared in
     the valu1 and value2     """
    if row_1 == row_2:
        return row_2

    for i in range(len(row_1)):
        if row_1[i] != row_2[i]:

            if row_1[i] == -1:
                row_1[i] = row_2[i]
            elif row_2[i] == -1:
                continue
            else:
                return # if problem with the check
    return row_1


def first_line_solution(constraints, start_bord):
    """ its make reverse and if there isnt start bord, its make one  """
    rows_number = len(constraints[0])
    check_index = 1
    row_side_sol = make_list_of_index(start_bord)
    new_lines = check_row_and_line(check_index, constraints, rows_number, [], row_side_sol)
    line_result = make_list_of_index(new_lines)
    return line_result


def check_row_and_line(index, constraints, line_number, tmp_solution, start_row):  ######################################################
    """
    :param index:
    :param constraints:
    :param line_number:
    :param tmp_solution:
    :param start_row:
    :return: posibale option for bord by check the row
    """
    tmp_result = []
    for i, value in enumerate(constraints[index]):
        if not (bool(value)):  #############
            tmp_solution.append([WHITE] * line_number) #########################################
            continue
        if len(value) == 1 and sum(value) == line_number:
            tmp_solution.append([BLACK] * line_number)###########################################
            continue
        else:
            if type(start_row[0]) is list:
                tmp_result = get_row_variations(start_row[i], value) ####################
            if not type(start_row[0]) is list:
                tmp_result = get_row_variations([-1] * line_number, value)#################
            if len(tmp_result) == 1:
                tmp_solution.append(tmp_result[0])
                continue
            if len(tmp_result) > 1:
                the_best_option = get_intersection_row(tmp_result)  ##### find from row_options the best option
                tmp_solution.append(the_best_option)
            else:
                tmp_solution.append([UNKNOWN] * line_number)
    return tmp_solution


#####################################################################^3


# get_row_variations(row, blocks): #func 1 real
def solve_nonogram(constraints):  #### func 4
    option = []
    return solve_nonogram_helper4(constraints, option, [])



def solve_nonogram_helper4(constraints, option, simple_result, num=0, first_enter=True):# helper func 4
    """
    :param constraints:
    :param option:
    :param simple_result:
    :param num:
    :param first_enter:
    :return:
    """
    global COUNT4
    global rows_option ########################################################
    if first_enter:

        simple_result = solve_easy_nonogram(constraints) ### solve easy
        if not rows_with_unknown_check(simple_result):
            return simple_result
    first_enter = False
    if not simple_result:
        return
    list_of_index = rows_with_unknown_check(simple_result) # list of the index of rows with -1

    if not list_of_index:
        if option:
            if check_if_results_same(option, simple_result):######################################
                return
        return option.append(simple_result)
    COUNT4 += 1
    index = list_of_index[num]
    if list_of_index:
        rows_option = get_row_variations(simple_result[index], constraints[0][index])
    for j in range(len(rows_option)): ###########################################################################################
        if UNKNOWN in rows_option[j] and rows_option[j][1:] == rows_option[j][:-1]: #   בדיקה אם הכל בשורה הוא -1 לא צריך לדעתי
            continue
        if rows_option[j] == simple_result[index]:
            continue
        simple_result[index] = rows_option[j]
        COUNT4 += 1
        simple_result = check_row_and_line(0, constraints, len(constraints[1]), [], simple_result)
        solve_nonogram_helper4(constraints, option, simple_result, 0, False)
        if j == len(rows_option) - 1 and index == list_of_index[-1]:
            return
    return option


def check_if_results_same(option, simple_result):##### למצוא דרך לייעל במהלך הבדיקה שהפונקציות זהות
    """ return TRUE if same else return false"""

    #check_if_results_same from line chack attnd row לא בטוח
    for i in option:
        if i == simple_result:
            return True
    return False



def rows_with_unknown_check(bord):
    """check if the bord contain -1
    :param bord: the list of list (the bord)
    :return: [] if the bord is full'
     else return list with the row index who contain -1"""
    rows_with_unknown = []
    if not bord:
        return
    for i, row in enumerate(bord):
        if UNKNOWN in row:
            rows_with_unknown.append(i)

    return rows_with_unknown


#############################################################^4
########################
def count_row_variations(length, blocks):
    num_block = len(blocks)
    the_amount_of_black = sum(blocks)
    k = length - the_amount_of_black - (num_block - 1)
    if k < 0:
        return 0
    n = length - the_amount_of_black + 1
    return int(binom_n_k(n, k))


def binom_n_k(n, k):
    f = math.factorial
    return f(n) / f(k) / f(n-k)


# print(count_row_variations(3, [1, 1]))
# print(count_row_variations(3, [2, 1]))

############################################################^555555
#
#
# WHITE_BLANK_REP = 0
# BLACK_BLANK_REP = 1
# WHITE_BLANK = "_"
# BLACK_BLANK = "▩"
# UNKNOWN_BLANK = "?"
# CHR_SEPARATOR = " "
# LINE_REGEX = "(?:[1]*)"
# LINE_SEPARATOR = " "
# REPLACE_FROM = "-1"
# REPLACE_TO = "0"
#
# def print_board(board):
#     """
#     This function prints the input board game to the screen.
#     :param board: The matrix that represents the game board.
#     :return: None
#     """
#     rep_str = ""
#     for row in board:
#         for blank in row:
#             if blank == WHITE_BLANK_REP:
#                 rep_str += WHITE_BLANK
#             elif blank == BLACK_BLANK_REP:
#                 rep_str += BLACK_BLANK
#             else:
#                 rep_str += UNKNOWN_BLANK
#             rep_str += CHR_SEPARATOR
#         rep_str += "\n"
#     print(rep_str)

# # ##############################
# def printer(x):
#     for i in x:
#         print()
#         print(i)


# ####################
#
# ###########################
# def len_checker(roows):
#     x = len(roows[-1])
#     for i in roows:
#         if len(i) != x:
#             print(False)
#     print(True)
#
# #########################
#
# def fine_if_equal(AAAA):
#     for i in AAAA:
#         if i == AAAA[-1]:
#             print('problem menn')


my_constraints=[ [ [], [4], [6], [2, 2], [1, 3] ], [ [1,3], [2], [1], [2, 2], [2, 2]]]
# print(first_row_solution(
#     [[[1, 1, 1], [5], [3], [1], [5]], [[2, 1], [2, 1], [5], [2, 1], [2, 1]]]))

# printer(first_line_solution([[[1, 1, 1], [5], [3], [1], [5]], [[2, 1], [2, 1], [5], [2, 1], [2, 1]]]))

R = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [-1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1], [1, 1, 1, 1, 1]]
LL = [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [1, 1, 1, 1, 1],
      [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]

L = [[[1, 1, 1], [5], [3], [1], [5]],
     [[2, 1], [2, 1], [5], [2, 1], [2, 1]]]  # my_constraints

MY_DROW = [
    [[1], [1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [2, 1, 2], [1, 3, 1], [1, 1, 1],
     [7]],
    [[1], [5], [1, 1, 1], [1, 1, 1], [1, 6], [1, 1, 1], [1, 1, 1], [5], [1]]]

CON_FOR4 = [[[1], [1]], [[1], [1]]]

# print(get_row_variations([-1, -1], [1]))

# print(first_line_solution(L, R))
# printer(solve_easy_nonogram(MY_DROW))
# printer(R)
# print(0)
# printer(LL)

def mast_be_bleck(row, block):
    """ func that return list of index that mast be black"""
    row_long = len(row)
    num_of_black = sum(block)
    block_length = len(block)
    if block_length == 1 and row_long/2 < num_of_black: ####const black
        start_indx = row_long - num_of_black
        end_indx = num_of_black - 1
        return list(range(start_indx, end_indx+1))
###################################4444444444444444444444444


# AAA= [[1],[2],[2],[2],[1],[1]],[[2],[2],[2],[3]]
# print(solve_nonogram(CON_FOR4))
# print(solve_nonogram(AAA))
# # print(solve_nonogram(MY_DROW))
# print(solve_easy_nonogram(AAA))
# print_board(solve_easy_nonogram([[[14,4,1],[12,4,7,1],[11,10,1],[11,1,3,5],[11,3,9],[13,4,8],[14,5,7],[14,5,7],[15,3,7],[13,3,7],[11,3,3,7],[10,9,2,1],[9,4,4,1,1],[8,3,6,2,1],[7,11,3,1],[6,3,3,2,3,1],[5,8,2,3,2],[3,2,3,3,3,3],[2,6,3,3,4],[1,2,3,2,5],[1,8,2,6],[2,1,8,2],[1,2,3,3,2,7],[4,2,2,2,6],[3,2,1,4,2],[5,3,2,3,5],[3,2,1,1,3,7],[1,3,3,2,2,8],[2,2,2,1,2,3],[1,2,2,2,3,6,2],[4,1,3,2,9,2],[2,2,2,1,8,2,2],[2,2,1,1,5,2,2],[1,1,3,3,2,1,2],[1,2,2,3,4,1,2],[5,2,2,2,6,2],[6,1,2,1,13]],[[16,3,3,2],[17,3,1,1,2,2],[18,3,2,2],[19,6,2,2],[19,6,2,3],[17,3,3,1],[15,3,2,3],[14,6,2,3],[13,7,1,3,2],[12,4,2,3,3,2],[11,3,1,2,2,2,2],[2,5,4,1,17],[1,5,3,3,4,2,2],[1,1,3,4,2,4,2],[1,1,2,4,2,2,3],[3,3,3,2,9],[6,2,3,2,3,6],[7,2,2,3,3,2,3],[3,3,7,2,3,3,1],[3,11,2,3,2,2],[1,1,9,2,3,3,3],[3,7,3,3,2,4],[2,1,3,3,2,4],[2,2,3,3,1,2,3],[1,8,3,2,2,2,2],[1,8,3,1,2,2,4,1],[1,8,3,2,2,3,5,1],[1,8,2,3,1,3,1],[8,1,4,1,4,1],[8,5,13],[21,13]]]))
# print_board(AAAA)
# # fine_if_equal(AAAA)
# print_board(solve_nonogram([[[6],[2,2,2],[2,3,2],[2,4,1],[1,2,2,1],[1,1,1],[1,2,2,2],[2,1,1,1,2],[1,2,2,1],[1,2,2,2],[6,2],[2,2,2],[1,1,3],[4,2,2],[1,6,1,1],[4,4,2],[2,2,2,2,1],[1,3,2],[1,1,1],[4,1]],[[2],[2],[5,2,3],[2,5,3],[2,1,1,1,2,1],[2,1,1,3,2,1,2],[1,5,3,1,1],[3,1,1,3,3,1],[5,1,3,2,2],[1,2,1,3,2,1],[1,1,1,1],[1,1,1,3,2],[2,1,3,2,1],[6,2,4,2],[3,1,2]]]))
# print_board(solve_nonogram([[[7],[7,1],[5,2],[5,1,1],[2,1,2,6,2],[6,1,2,2,1],[9,4,2],[3,1,1,2,3,1],[1,3,3,1,1,3,2],[1,2,1,2,1,2,4,1],[1,4,1,3,1,3,1],[1,2,3,2,2,3,1],[4,2,1,5,2],[2,4,3],[2]],[[1,2],[2,1,3],[1,1,1,1,2],[1,1,1,5],[1,1,1,3],[1,1,1,1],[11],[3,1,1],[3,1,2],[5,1,1],[3,8],[2,1,2,3],[2,2,1,1,2],[1,2,6],[2,1,1,4],[3,2,1],[1,1,1,1],[1,1,6],[1,2,1,1],[1,6,1],[6,1],[2,3,1],[1,1,1,1],[4,1],[2]]]))
######3333
# print_board(solve_easy_nonogram(AAA))
# len_checker(solve_easy_nonogram(MY_DROW))

 # func 1 tests
# print(1)
# print(get_row_variations([1,1,-1,0],[3]))
# print(2)
# print(get_row_variations([-1,-1,-1,0],[2]))
# print(3)
# print(get_row_variations([-1,0,1,0,-1,0],[1,1]))
# print(4)
# print(get_row_variations([-1,-1,-1],[1]))
# print(5)
# print(get_row_variations([0,0,0],[1]))
# print(6)
# print(get_row_variations([0,0,-1,1,0],[3]))
# print(7)
# print(get_row_variations([0,0,-1,1,0],[2]))
# print(8)
# print(get_row_variations([0,0,1,1,0],[2]))
# print(9)
# print(get_row_variations([-1,-1,-1,-1,-1,-1, -1, -1, -1], [7]))
#
# print(compre_list(R[0], LL[0]))
# make_list_of_index([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#
#

# print(row_check([1,1], [2], 2, 3))
# print(get_intersection_row([[1, 0,1], [0, -1, 0]]))

# print(check_for_get_row_variations([1, 0], [1, 1], 1))
# print(get_row_variations([[-1,-1,-1,-1,-1]], [1,3]))
# print(get_row_variations([1, 1, -1, 0], [3]))
#
# print(get_row_variations([-1]*7, [5]))
#
# print(COUNT)
# print(COUNT4)

# mast_be_bleck([-1]*7, [4])


COUNT = 0 ###########################  לזכור למחוק !!!!!!!!
COUNT4 = 0
BLACK = 1
WHITE = 0
UNKNOWN = -1

import math
#################################### יעילות לפי אורך שורה

# count_row_variations(length, blocks)

def helper_get_row_variations(row, blocks, tmp_lst, row_lst, index, first_enter=True):  # func 1 helper
    global COUNT
    length = len(row)
    #
    if first_enter:
        found_common_cases = common_cases(row, blocks)
        if found_common_cases:
            answer = get_intersection_row([row, found_common_cases])
            if not rows_with_unknown_check([answer]):
                return [found_common_cases]


    if sum(blocks) - sum(tmp_lst) > len(row) - len(tmp_lst):
        return
    if tmp_lst.count(BLACK) > sum(blocks):
        return
    if index > 1 and not row_check(tmp_lst, blocks, index, length):
        return
    if len(row_lst) == count_row_variations(length, blocks):
        return row_lst
    if len(tmp_lst) == length:
        if tmp_lst.count(BLACK) != sum(blocks):
            return
        return row_lst.append(tmp_lst)
    COUNT += 1
    if row[index] == UNKNOWN:
        tmp_lst.append(BLACK)
        helper_get_row_variations(row, blocks, tmp_lst[:], row_lst, index + 1, False)
        tmp_lst[-1] = WHITE
        helper_get_row_variations(row, blocks, tmp_lst[:], row_lst, index + 1, False)
    else:
        tmp_lst.append(row[index])
        helper_get_row_variations(row, blocks, tmp_lst[:], row_lst, index + 1, False)
    return row_lst


def common_cases(row, block):
    row_long = len(row)
    num_of_black = sum(block)
    block_length = len(block)
    lst = []
    if num_of_black + len(block) - 1 == row_long:   ################################# make the only row thets posibaol
        for i, value in enumerate(block):
            lst.extend([BLACK] * value)
            if i != block_length - 1:
                lst.append(WHITE)
        return lst
    if not block: ### zero row
        return lst.extend([WHITE] * row_long)
    if block_length == 1 and num_of_black == row_long:  ## all black
        return lst.extend([BLACK] * row_long)

    # if block_length == 1 and row_long/2 <num_of_black: ####const black
    #     start_i_black = row_long - num_of_black
    #     # end_i_black = num_of_black -1
    #     add_amount = num_of_black - start_i_black
    #     for i in range(row_long):
    #         if i == start_i_black:
    #             lst.extend([BLACK] * add_amount)
    #             i += add_amount
    #         else:
    #             lst.append(UNKNOWN)
    #     return lst



def row_check(tmp_lst, blocks, index, lenght):  # func 1
    """
    :return True if the checks is ok
    :param tmp_lst:
    :param blocks:
    :return:
    """
    counter = 0
    b_num = 0
    block_check = blocks[b_num]
    for i, v in enumerate(tmp_lst):
        if i != index - 1: # check if first?
            if v == BLACK:
                counter += 1
                if tmp_lst[i + 1] == 0:
                    if blocks[b_num] != counter:
                        return False
                    else:
                        counter = 0
                        b_num += 1
        else:
            if v == BLACK:
                counter += 1
                if blocks[b_num] != counter and not i < lenght - 1:  ##
                    return False
    return True


def get_row_variations(row, blocks): #func 1 real
    return helper_get_row_variations(row, blocks, [], [], 0)


####################################################################^1

def make_list_of_index(rows):
    lenght = len(rows[0])
    n = len(rows)
    tmp_lst = []
    list_of_index = []
    for i in range(lenght):  # line
        if i != 0:
            list_of_index.append(tmp_lst)
            tmp_lst = []
        for j in range(n):  # row external
            tmp_lst.append(rows[j][i])
    list_of_index.append(tmp_lst)
    return list_of_index


def get_intersection_row(rows):  # func 2
    """ recive list of list (option for one row) and return the option for
    the row
    זה עובר על אינדקסים של השורות
    i choose that this func return only what is 100% right"""

    the_rows = make_list_of_index(rows)
    result = []
    for i in range(len(the_rows)):
        if all(x == the_rows[i][0] for x in the_rows[i]): ###IF ALL THE SAME
            result.append(the_rows[i][0])
            continue
        if 0 in the_rows[i] and (1 or -1) in the_rows[i]:
            result.append(UNKNOWN)
            continue
        result.append(UNKNOWN)

    return result


#########################################################################^2

############################################################################

def solve_easy_nonogram(constraints):  ## main
    """make the firs check and then cotinue to check if it not redey"""
    # empty_list = []
    bord = find_start_bord(constraints)
    return helper_func3(constraints, bord)


def find_start_bord(constraints):
    """
    make mat
    :param constraints:
    :return:
    """
    line_num = len(constraints[1])
    row_num = len(constraints[0])
    first_bord = []
    for i in range(row_num):
        tmp = []
        tmp.extend([UNKNOWN] * line_num)
        first_bord.append(tmp)
    return first_bord


def helper_func3(constraints, start_bord):
    global COUNT
    line_solution = first_line_solution(constraints, start_bord)
    row_solution = first_row_solution(constraints, line_solution)
    if row_solution == line_solution:
        return row_solution
    make_2_check_loops = 2
    while make_2_check_loops:
        COUNT += 1 ####
        tmp_lst = []
        for i in range(len(row_solution)):
            end_com_result = compre_list(row_solution[i], line_solution[i])
            tmp_lst.append(end_com_result)
        row_solution = first_row_solution(constraints, tmp_lst)
        line_solution = first_line_solution(constraints, row_solution)
        if row_solution != line_solution:
            make_2_check_loops = 2
        else:
            make_2_check_loops -= 1
            if make_2_check_loops == 0:
                break

    return line_solution



def first_row_solution(constraints, list_of_rows):
    line_number = len(constraints[1])
    check_index = 0
    return check_row_and_line(check_index, constraints, line_number, [],
                              list_of_rows)



def compre_list(row_1, row_2):
    """ compere two list if value1 is -1 and value2 is 1 or 0 the function
    chage value1 to 1 or 0, the function return the number of -1 appeared in
     the valu1 and value2     """
    if row_1 == row_2:
        return row_2

    for i in range(len(row_1)):
        if row_1[i] != row_2[i]:

            if row_1[i] == -1:
                row_1[i] = row_2[i]
            elif row_2[i] == -1:
                continue
            else:
                return # if problem with the check
    return row_1


def first_line_solution(constraints, start_bord):
    """ its make reverse and if there isnt start bord, its make one  """
    rows_number = len(constraints[0])
    check_index = 1
    row_side_sol = make_list_of_index(start_bord)
    new_lines = check_row_and_line(check_index, constraints, rows_number, [], row_side_sol)
    line_result = make_list_of_index(new_lines)
    return line_result


def check_row_and_line(index, constraints, line_number, tmp_solution, start_row):  ######################################################
    """
    :param index:
    :param constraints:
    :param line_number:
    :param tmp_solution:
    :param start_row:
    :return: posibale option for bord by check the row
    """
    tmp_result = []
    for i, value in enumerate(constraints[index]):
        if not (bool(value)):  #############
            tmp_solution.append([WHITE] * line_number) #########################################
            continue
        if len(value) == 1 and sum(value) == line_number:
            tmp_solution.append([BLACK] * line_number)###########################################
            continue
        else:
            if type(start_row[0]) is list:
                tmp_result = get_row_variations(start_row[i], value) ####################
            if not type(start_row[0]) is list:
                tmp_result = get_row_variations([-1] * line_number, value)#################
            if len(tmp_result) == 1:
                tmp_solution.append(tmp_result[0])
                continue
            if len(tmp_result) > 1:
                the_best_option = get_intersection_row(tmp_result)  ##### find from row_options the best option
                tmp_solution.append(the_best_option)
            else:
                tmp_solution.append([UNKNOWN] * line_number)
    return tmp_solution


#####################################################################^3


# get_row_variations(row, blocks): #func 1 real
def solve_nonogram(constraints):  #### func 4
    option = []
    return solve_nonogram_helper4(constraints, option, [])



def solve_nonogram_helper4(constraints, option, simple_result, num=0, first_enter=True):# helper func 4
    """
    :param constraints:
    :param option:
    :param simple_result:
    :param num:
    :param first_enter:
    :return:
    """
    global COUNT4
    # global rows_option ########################################################
    if first_enter:
        simple_result = solve_easy_nonogram(constraints) ### solve easy
        if not rows_with_unknown_check(simple_result):
            return simple_result
    first_enter = False
    if not simple_result:
        return
    list_of_index = rows_with_unknown_check(simple_result) # list of the index of rows with -1

    if not list_of_index:
        if option:
            if check_if_results_same(option, simple_result):######################################
                return
        return option.append(simple_result)

    index = list_of_index[num]
    if list_of_index:
        rows_option = get_row_variations(simple_result[index], constraints[0][index])
    for j in range(len(rows_option)): ###########################################################################################
        if UNKNOWN in rows_option[j] and rows_option[j][1:] == rows_option[j][:-1]: #   בדיקה אם הכל בשורה הוא -1 לא צריך לדעתי
            continue
        if rows_option[j] == simple_result[index]:
            continue
        simple_result[index] = rows_option[j]
        COUNT4 += 1
        simple_result = check_row_and_line(0, constraints, len(constraints[1]), [], simple_result)
        solve_nonogram_helper4(constraints, option, simple_result, 0, False)
        if j == len(rows_option) - 1 and index == list_of_index[-1]:
            return
    return option


def check_if_results_same(option, simple_result):##### למצוא דרך לייעל במהלך הבדיקה שהפונקציות זהות
    """ return TRUE if same else return false"""

    #check_if_results_same from line chack attnd row לא בטוח
    for i in option:
        if i == simple_result:
            return True
    return False



def rows_with_unknown_check(bord):
    """check if the bord contain -1
    :param bord: the list of list (the bord)
    :return: [] if the bord is full'
     else return list with the row index who contain -1"""
    rows_with_unknown = []
    if not bord:
        return
    for i, row in enumerate(bord):
        if UNKNOWN in row:
            rows_with_unknown.append(i)

    return rows_with_unknown


#############################################################^4
########################
def count_row_variations(length, blocks):
    num_block = len(blocks)
    the_amount_of_black = sum(blocks)
    k = length - the_amount_of_black - (num_block - 1)
    if k < 0:
        return 0
    n = length - the_amount_of_black + 1
    return int(binom_n_k(n, k))


def binom_n_k(n, k):
    f = math.factorial
    return f(n) / f(k) / f(n-k)


# print(count_row_variations(3, [1, 1]))
# print(count_row_variations(3, [2, 1]))

############################################################^555555
#
# #
# WHITE_BLANK_REP = 0
# BLACK_BLANK_REP = 1
# WHITE_BLANK = "_"
# BLACK_BLANK = "X"
# UNKNOWN_BLANK = "?"
# CHR_SEPARATOR = " "
# LINE_REGEX = "(?:[1]*)"
# LINE_SEPARATOR = " "
# REPLACE_FROM = "-1"
# REPLACE_TO = "0"
#
# def print_board(board):
#     """
#     This function prints the input board game to the screen.
#     :param board: The matrix that represents the game board.
#     :return: None
#     """
#     rep_str = ""
#     for row in board:
#         for blank in row:
#             if blank == WHITE_BLANK_REP:
#                 rep_str += WHITE_BLANK
#             elif blank == BLACK_BLANK_REP:
#                 rep_str += BLACK_BLANK
#             else:
#                 rep_str += UNKNOWN_BLANK
#             rep_str += CHR_SEPARATOR
#         rep_str += "\n"
#     print(rep_str)
#
# # ##############################
# def printer(x):
#     for i in x:
#         print()
#         print(i)


# ####################
#
# ###########################
# def len_checker(roows):
#     x = len(roows[-1])
#     for i in roows:
#         if len(i) != x:
#             print(False)
#     print(True)
#
# #########################
#
# def fine_if_equal(AAAA):
#     for i in AAAA:
#         if i == AAAA[-1]:
#             print('problem menn')


my_constraints=[ [ [], [4], [6], [2, 2], [1, 3] ], [ [1,3], [2], [1], [2, 2], [2, 2]]]
# print(first_row_solution(
#     [[[1, 1, 1], [5], [3], [1], [5]], [[2, 1], [2, 1], [5], [2, 1], [2, 1]]]))

# printer(first_line_solution([[[1, 1, 1], [5], [3], [1], [5]], [[2, 1], [2, 1], [5], [2, 1], [2, 1]]]))

R = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [-1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1], [1, 1, 1, 1, 1]]
LL = [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [1, 1, 1, 1, 1],
      [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]

L = [[[1, 1, 1], [5], [3], [1], [5]],
     [[2, 1], [2, 1], [5], [2, 1], [2, 1]]]  # my_constraints

MY_DROW = [
    [[1], [1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [2, 1, 2], [1, 3, 1], [1, 1, 1],
     [7]],
    [[1], [5], [1, 1, 1], [1, 1, 1], [1, 6], [1, 1, 1], [1, 1, 1], [5], [1]]]

CON_FOR4 = [[[1], [1]], [[1], [1]]]

# print(get_row_variations([-1, -1], [1]))

# print(first_line_solution(L, R))
# printer(solve_easy_nonogram(MY_DROW))
# printer(R)
# print(0)
# printer(LL)


###################################4444444444444444444444444


AAA= [[1],[2],[2],[2],[1],[1]],[[2],[2],[2],[3]]
# print(solve_nonogram(CON_FOR4))
# printer(solve_nonogram(AAA))
# print(solve_nonogram(MY_DROW))
# print_board(solve_easy_nonogram(MY_DROW))

# print_board(AAAA)
# # fine_if_equal(AAAA)


######3333
# print_board(solve_easy_nonogram(AAA))
# len_checker(solve_easy_nonogram(MY_DROW))

 # func 1 tests
# print(1)
# print(get_row_variations([1,1,-1,0],[3]))
# print(2)
# print(get_row_variations([-1,-1,-1,0],[2]))
# print(3)
# print(get_row_variations([-1,0,1,0,-1,0],[1,1]))
# print(4)
# print(get_row_variations([-1,-1,-1],[1]))
# print(5)
# print(get_row_variations([0,0,0],[1]))
# print(6)
# print(get_row_variations([0,0,-1,1,0],[3]))
# print(7)
# print(get_row_variations([0,0,-1,1,0],[2]))
# print(8)
# print(get_row_variations([0,0,1,1,0],[2]))
# print(9)
# print(get_row_variations([-1,-1,-1,-1,-1,-1, -1, -1, -1], [7]))
#
# print(compre_list(R[0], LL[0]))
# make_list_of_index([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#
#

# print(row_check([1,1], [2], 2, 3))
# print(get_intersection_row([[1, 0,1], [0, -1, 0]]))

# print(check_for_get_row_variations([1, 0], [1, 1], 1))
# print(get_row_variations([[-1,-1,-1,-1,-1]], [1,3]))
# print(get_row_variations([1, 1, -1, 0], [3]))
#
# print(COUNT)
# print(CON_FOR4)





################################################################## גרסה אחרונה
COUNT = 0 ###########################  לזכור למחוק !!!!!!!!
BLACK = 1
WHITE = 0
UNKNOWN = -1

import math
#################################### יעילות לפי אורך שורה

# count_row_variations(length, blocks)

def helper_get_row_variations(row, blocks, tmp_lst, row_lst, index, first_enter=True):  # func 1 helper
    # global COUNT
    length = len(row)
    #
    if first_enter:
        found_common_cases = common_cases(row, blocks)
        if found_common_cases:
            answer = get_intersection_row([row, found_common_cases])
            if not rows_with_unknown_check([answer]):
                return [found_common_cases]

    if len(row_lst) == count_row_variations(length, blocks):
        return row_lst
    if sum(blocks) - sum(tmp_lst) > len(row) - len(tmp_lst):
        return
    if tmp_lst.count(BLACK) > sum(blocks):
        return
    if index > 1 and not row_check(tmp_lst, blocks, index, length):
        return
    if len(tmp_lst) == length:
        if tmp_lst.count(BLACK) != sum(blocks):
            return

        return row_lst.append(tmp_lst)
    # COUNT += 1
    if row[index] == UNKNOWN:
        tmp_lst.append(BLACK)
        helper_get_row_variations(row, blocks, tmp_lst[:], row_lst, index + 1, False)
        tmp_lst[-1] = WHITE
        helper_get_row_variations(row, blocks, tmp_lst[:], row_lst, index + 1, False)
    else:
        tmp_lst.append(row[index])
        helper_get_row_variations(row, blocks, tmp_lst[:], row_lst, index + 1, False)
    return row_lst


def common_cases(row, block):
    row_long = len(row)
    num_of_black = sum(block)
    block_length = len(block)
    lst = []
    if num_of_black + len(block) - 1 == row_long:   ################################# make the only row thets posibaol
        for i, value in enumerate(block):
            lst.extend([BLACK] * value)
            if i != block_length - 1:
                lst.append(WHITE)
        return lst
    if not block: ### zero row
        return lst.extend([WHITE] * row_long)
    if block_length == 1 and num_of_black == row_long:  ## all black
        return lst.extend([BLACK] * row_long)

    # if block_length == 1 and row_long/2 <num_of_black: ####const black
    #     start_i_black = row_long - num_of_black
    #     # end_i_black = num_of_black -1
    #     add_amount = num_of_black - start_i_black
    #     for i in range(row_long):
    #         if i == start_i_black:
    #             lst.extend([BLACK] * add_amount)
    #             i += add_amount
    #         else:
    #             lst.append(UNKNOWN)
    #     return lst



def row_check(tmp_lst, blocks, index, lenght):  # func 1
    """
    :return True if the checks is ok
    :param tmp_lst:
    :param blocks:
    :return:
    """
    counter = 0
    b_num = 0
    block_check = blocks[b_num]
    for i, v in enumerate(tmp_lst):
        if i != index - 1: # check if first?
            if v == BLACK:
                counter += 1
                if tmp_lst[i + 1] == 0:
                    if blocks[b_num] != counter:
                        return False
                    else:
                        counter = 0
                        b_num += 1
        else:
            if v == BLACK:
                counter += 1
                if blocks[b_num] != counter and not i < lenght - 1:  ##
                    return False
    return True


def get_row_variations(row, blocks): #func 1 real
    return helper_get_row_variations(row, blocks, [], [], 0)


####################################################################^1

def make_list_of_index(rows):
    lenght = len(rows[0])
    n = len(rows)
    tmp_lst = []
    list_of_index = []
    for i in range(lenght):  # line
        if i != 0:
            list_of_index.append(tmp_lst)
            tmp_lst = []
        for j in range(n):  # row external
            tmp_lst.append(rows[j][i])
    list_of_index.append(tmp_lst)
    return list_of_index


def get_intersection_row(rows):  # func 2
    """ recive list of list (option for one row) and return the option for
    the row
    זה עובר על אינדקסים של השורות
    i choose that this func return only what is 100% right"""

    the_rows = make_list_of_index(rows)
    result = []
    for i in range(len(the_rows)):
        if all(x == the_rows[i][0] for x in the_rows[i]): ###IF ALL THE SAME
            result.append(the_rows[i][0])
            continue
        if 0 in the_rows[i] and (1 or -1) in the_rows[i]:
            result.append(UNKNOWN)
            continue
        result.append(UNKNOWN)

    return result


#########################################################################^2

############################################################################

def solve_easy_nonogram(constraints):  ## main
    """make the firs check and then cotinue to check if it not redey"""
    # empty_list = []
    bord = find_start_bord(constraints)
    return helper_func3(constraints, bord)


def find_start_bord(constraints):
    """
    make mat
    :param constraints:
    :return:
    """
    line_num = len(constraints[1])
    row_num = len(constraints[0])
    first_bord = []
    for i in range(row_num):
        tmp = []
        tmp.extend([UNKNOWN] * line_num)
        first_bord.append(tmp)
    return first_bord


def helper_func3(constraints, start_bord):
    global COUNT
    line_solution = first_line_solution(constraints, start_bord)
    row_solution = first_row_solution(constraints, line_solution)
    if row_solution == line_solution:
        return row_solution
    make_2_check_loops = 2
    while make_2_check_loops:
        COUNT += 1 ####
        tmp_lst = []
        for i in range(len(row_solution)):
            end_com_result = compre_list(row_solution[i], line_solution[i])
            tmp_lst.append(end_com_result)
        row_solution = first_row_solution(constraints, tmp_lst)
        line_solution = first_line_solution(constraints, row_solution)
        if row_solution != line_solution:
            make_2_check_loops = 2
        else:
            make_2_check_loops -= 1
            if make_2_check_loops == 0:
                break

    return line_solution



def first_row_solution(constraints, list_of_rows):
    line_number = len(constraints[1])
    check_index = 0
    return check_row_and_line(check_index, constraints, line_number, [],
                              list_of_rows)



def compre_list(row_1, row_2):
    """ compere two list if value1 is -1 and value2 is 1 or 0 the function
    chage value1 to 1 or 0, the function return the number of -1 appeared in
     the valu1 and value2     """
    if row_1 == row_2:
        return row_2

    for i in range(len(row_1)):
        if row_1[i] != row_2[i]:

            if row_1[i] == -1:
                row_1[i] = row_2[i]
            elif row_2[i] == -1:
                continue
            else:
                return # if problem with the check
    return row_1


def first_line_solution(constraints, start_bord):
    """ its make reverse and if there isnt start bord, its make one  """
    rows_number = len(constraints[0])
    check_index = 1
    row_side_sol = make_list_of_index(start_bord)
    new_lines = check_row_and_line(check_index, constraints, rows_number, [], row_side_sol)
    line_result = make_list_of_index(new_lines)
    return line_result


def check_row_and_line(index, constraints, line_number, tmp_solution, start_row):  ######################################################
    """
    :param index:
    :param constraints:
    :param line_number:
    :param tmp_solution:
    :param start_row:
    :return: posibale option for bord by check the row
    """
    tmp_result = []
    for i, value in enumerate(constraints[index]):
        if not (bool(value)):  #############
            tmp_solution.append([WHITE] * line_number) #########################################
            continue
        if len(value) == 1 and sum(value) == line_number:
            tmp_solution.append([BLACK] * line_number)###########################################
            continue
        else:
            if type(start_row[0]) is list:
                tmp_result = get_row_variations(start_row[i], value) ####################
            if not type(start_row[0]) is list:
                tmp_result = get_row_variations([-1] * line_number, value)#################
            if len(tmp_result) == 1:
                tmp_solution.append(tmp_result[0])
                continue
            if len(tmp_result) > 1:
                the_best_option = get_intersection_row(tmp_result)  ##### find from row_options the best option
                tmp_solution.append(the_best_option)
            else:
                tmp_solution.append([UNKNOWN] * line_number)
    return tmp_solution


#####################################################################^3


# get_row_variations(row, blocks): #func 1 real
def solve_nonogram(constraints):  #### func 4
    option = []
    return solve_nonogram_helper4(constraints, option, [])



def solve_nonogram_helper4(constraints, option, simple_result, num=0, first_enter=True):# helper func 4
    """
    :param constraints:
    :param option:
    :param simple_result:
    :param num:
    :param first_enter:
    :return:
    """
    global rows_option ########################################################
    if first_enter:
        simple_result = solve_easy_nonogram(constraints) ### משתמש בפונק' 3 ומוציא לוח
        first_enter = False
    if not simple_result: # מוודא שזה לא לוח ריק
        return
    list_of_index = rows_with_unknown_check(simple_result) # רשימה אינדקסים של השורות הבעייתיים

    if not list_of_index:
        if option:
            if check_if_results_same(option, simple_result):
                return
        return option.append(simple_result)

    index = list_of_index[num]
    if list_of_index:
        rows_option = get_row_variations(simple_result[index], constraints[0][index])
    for j in range(len(rows_option)): ###########################################################################################
        if UNKNOWN in rows_option[j] and rows_option[j][1:] == rows_option[j][:-1]: #   בדיקה אם הכל בשורה הוא -1 לא צריך לדעתי
            continue
        if rows_option[j] == simple_result[index]:
            continue
        simple_result[index] = rows_option[j]
        simple_result = check_row_and_line(0, constraints, len(constraints[1]), [], simple_result)
        solve_nonogram_helper4(constraints, option, simple_result, num, False)
        if j == len(rows_option) - 1 and index == list_of_index[-1]:
            return
    return option


def check_if_results_same(option, simple_result):##### למצוא דרך לייעל במהלך הבדיקה שהפונקציות זהות
    """ return TRUE if same else return false"""

    #check_if_results_same from line chack attnd row לא בטוח
    for i in option:
        if i == simple_result:
            return True
    return False



def rows_with_unknown_check(bord):
    """check if the bord contain -1
    :param bord: the list of list (the bord)
    :return: [] if the bord is full'
     else return list with the row index who contain -1"""
    rows_with_unknown = []
    if not bord:
        return
    for i, row in enumerate(bord):
        if UNKNOWN in row:
            rows_with_unknown.append(i)

    return rows_with_unknown


#############################################################^4
########################
def count_row_variations(length, blocks):
    num_block = len(blocks)
    the_amount_of_black = sum(blocks)
    k = length - the_amount_of_black - (num_block - 1)
    if k < 0:
        return 0
    n = length - the_amount_of_black + 1
    return int(binom_n_k(n, k))


def binom_n_k(n, k):
    f = math.factorial
    return f(n) / f(k) / f(n-k)


# print(count_row_variations(3, [1, 1]))
# print(count_row_variations(3, [2, 1]))

############################################################^555555

#
# WHITE_BLANK_REP = 0
# BLACK_BLANK_REP = 1
# WHITE_BLANK = "_"
# BLACK_BLANK = "X"
# UNKNOWN_BLANK = "?"
# CHR_SEPARATOR = " "
# LINE_REGEX = "(?:[1]*)"
# LINE_SEPARATOR = " "
# REPLACE_FROM = "-1"
# REPLACE_TO = "0"
#
# def print_board(board):
#     """
#     This function prints the input board game to the screen.
#     :param board: The matrix that represents the game board.
#     :return: None
#     """
#     rep_str = ""
#     for row in board:
#         for blank in row:
#             if blank == WHITE_BLANK_REP:
#                 rep_str += WHITE_BLANK
#             elif blank == BLACK_BLANK_REP:
#                 rep_str += BLACK_BLANK
#             else:
#                 rep_str += UNKNOWN_BLANK
#             rep_str += CHR_SEPARATOR
#         rep_str += "\n"
#     print(rep_str)
#
# ##############################
# def printer(x):
#     for i in x:
#         print()
#         print(i)
#

# ####################
#
# ###########################
# def len_checker(roows):
#     x = len(roows[-1])
#     for i in roows:
#         if len(i) != x:
#             print(False)
#     print(True)
#
# #########################
#
# def fine_if_equal(AAAA):
#     for i in AAAA:
#         if i == AAAA[-1]:
#             print('problem menn')


my_constraints=[ [ [], [4], [6], [2, 2], [1, 3] ], [ [1,3], [2], [1], [2, 2], [2, 2]]]
# print(first_row_solution(
#     [[[1, 1, 1], [5], [3], [1], [5]], [[2, 1], [2, 1], [5], [2, 1], [2, 1]]]))

# printer(first_line_solution([[[1, 1, 1], [5], [3], [1], [5]], [[2, 1], [2, 1], [5], [2, 1], [2, 1]]]))

R = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [-1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1], [1, 1, 1, 1, 1]]
LL = [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [1, 1, 1, 1, 1],
      [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]

L = [[[1, 1, 1], [5], [3], [1], [5]],
     [[2, 1], [2, 1], [5], [2, 1], [2, 1]]]  # my_constraints

MY_DROW = [
    [[1], [1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [2, 1, 2], [1, 3, 1], [1, 1, 1],
     [7]],
    [[1], [5], [1, 1, 1], [1, 1, 1], [1, 6], [1, 1, 1], [1, 1, 1], [5], [1]]]

CON_FOR4 = [[[1], [1]], [[1], [1]]]

# print(get_row_variations([-1, -1], [1]))

# print(first_line_solution(L, R))
# printer(solve_easy_nonogram(MY_DROW))
# printer(R)
# print(0)
# printer(LL)


###################################          4444444444444444444444444


# AAA= [[1],[2],[2],[2],[1],[1]],[[2],[2],[2],[3]]
# printer(solve_nonogram(CON_FOR4))
#
# AAAA = solve_easy_nonogram(MY_DROW)
# print_board(AAAA)
# # fine_if_equal(AAAA)


######3333
# print_board(solve_easy_nonogram(AAA))
# len_checker(solve_easy_nonogram(MY_DROW))

 # func 1 tests
# print(1)
# print(get_row_variations([1,1,-1,0],[3]))
# print(2)
# print(get_row_variations([-1,-1,-1,0],[2]))
# print(3)
# print(get_row_variations([-1,0,1,0,-1,0],[1,1]))
# print(4)
# print(get_row_variations([-1,-1,-1],[1]))
# print(5)
# print(get_row_variations([0,0,0],[1]))
# print(6)
# print(get_row_variations([0,0,-1,1,0],[3]))
# print(7)
# print(get_row_variations([0,0,-1,1,0],[2]))
# print(8)
# print(get_row_variations([0,0,1,1,0],[2]))
# print(9)
# print(get_row_variations([-1,-1,-1,-1,-1,-1, -1, -1, -1], [7]))
#
# print(compre_list(R[0], LL[0]))
# make_list_of_index([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#
#

# print(row_check([1,1], [2], 2, 3))
# print(get_intersection_row([[1, 0,1], [0, -1, 0]]))

# print(check_for_get_row_variations([1, 0], [1, 1], 1))
# print(get_row_variations([[-1,-1,-1,-1,-1]], [1,3]))
# print(get_row_variations([1, 1, -1, 0], [3]))
#
# print(COUNT)























COUNT = 0
BLACK = 1
WHITE = 0
UNKNOWN = -1

#################################### יעילות לפי אורך שורה


def helper_get_row_variations(row, blocks, tmp_lst, row_lst, index):  # func 1 helper
    global COUNT
    # print(index)
    lenght = len(row)

    if index == 0:
        found_common_cases = common_cases(row, blocks)
        if found_common_cases:
            answer = get_intersection_row([row, found_common_cases])
            if not rows_with_unknown_check([answer]):
                return [found_common_cases]

    if sum(blocks) - sum(tmp_lst) > len(row) - len(tmp_lst):##################
        return
    if tmp_lst.count(1) > sum(blocks):
        return
    if index > 1 and not row_check(tmp_lst, blocks, index, lenght):
        return
    if len(tmp_lst) == lenght:
        if tmp_lst.count(1) != sum(blocks):
            return
        return row_lst.append(tmp_lst)
    COUNT += 1
    if row[index] == UNKNOWN:
        tmp_lst.append(BLACK)
        helper_get_row_variations(row, blocks, tmp_lst[:], row_lst, index + 1)
        tmp_lst[-1] = WHITE
        helper_get_row_variations(row, blocks, tmp_lst[:], row_lst, index + 1)
    else:
        tmp_lst.append(row[index])
        helper_get_row_variations(row, blocks, tmp_lst[:], row_lst,
                                  index + 1)
    # print(1)
    return row_lst


def common_cases(row, block):
    row_long = len(row)
    num_of_black = sum(block)
    block_length = len(block)
    lst = []
    if num_of_black + len(block) - 1 == row_long:
        for i, value in enumerate(block):
            lst.extend([1] * value)
            if i != block_length - 1:
                lst.append(0)
        return lst
    if not block: ### zero row
        return lst.extend([0] * row_long)
    if num_of_black == row_long:  ## all black
        return lst.extend([1] *row_long)



    # if sum(blocks) = le###    all black option




def row_check(tmp_lst, blocks, index, lenght):  # func 1
    """
    :return True if the checks is ok
    :param tmp_lst:
    :param blocks:
    :return:
    """
    counter = 0
    b_num = 0
    block_check = blocks[b_num]
    # print('row_check')
    for i, v in enumerate(tmp_lst):
        if i != index - 1: # check if first?
            if v == BLACK:
                counter += 1
                if tmp_lst[i + 1] == 0:
                    if blocks[b_num] != counter:
                        return False
                    else:
                        counter = 0
                        b_num += 1
        else:
            if v == BLACK:
                counter += 1
                if blocks[b_num] != counter and not i < lenght - 1:  ##
                    return False
    return True


def get_row_variations(row, blocks): #func 1 real
    return helper_get_row_variations(row, blocks, [], [], 0)


####################################################################^1

def make_list_of_index(rows):
    lenght = len(rows[0])
    n = len(rows)
    tmp_lst = []
    list_of_index = []
    for i in range(lenght):  # line
        if i != 0:
            list_of_index.append(tmp_lst)
            tmp_lst = []
        for j in range(n):  # row external
            tmp_lst.append(rows[j][i])
    list_of_index.append(tmp_lst)
    return list_of_index


def get_intersection_row(rows):  # func 2
    """ recive list of list (option for one row) and return the option for
    the row
    i choose that this func return only what is 100% right"""

    the_rows = make_list_of_index(rows)
    result = []
    for i in range(len(the_rows)):
        if all(x == the_rows[i][0] for x in the_rows[i]): ###
            result.append(the_rows[i][0])
            continue
        if 0 in the_rows[i] and (1 or -1) in the_rows[i]:
            result.append(-1)
            continue
        if (-1 and 1) in the_rows[i] and 0 not in the_rows[i]:
            if (the_rows[i].count(1)) // 2 >= the_rows[i].count(-1):
                result.append(-1)  #### meantime
                continue
            result.append(-1)
        else:
            result.append(-1)
    return result


#########################################################################^2

############################################################################

def solve_easy_nonogram(constraints):  ## main
    """make the firs check and then cotinue to check if it not redey"""
    # empty_list = []
    bord = find_start_bord(constraints)
    return helper_func3(constraints, bord)


def find_start_bord(constraints):
    """
    make mat
    :param constraints:
    :return:
    """
    line_num = len(constraints[1])
    row_num = len(constraints[0])
    first_bord = []
    for i in range(row_num):
        tmp = []
        tmp.extend([-1] * line_num)
        first_bord.append(tmp)
    return first_bord



def helper_func3(constraints, start_bord):

    line_solution = first_line_solution(constraints, start_bord)
    row_solution = first_row_solution(constraints, line_solution)
    if row_solution == line_solution:
        return row_solution
    new_lst = []
    make_2_check_loops = 2

    while make_2_check_loops:
        # printer(line_solution)
        new_lst = [] ################################################################## פה
        for i in range(len(row_solution)):
            x = compre_list(row_solution[i], line_solution[i])
            new_lst.append(x)
        row_solution = first_row_solution(constraints, new_lst)
        line_solution = first_line_solution(constraints, row_solution)
        print('ofir the king')
        if row_solution != line_solution:
            make_2_check_loops = 2
        else:
            if make_2_check_loops == 0:
                print('out')
                break
            make_2_check_loops -= 1

    return line_solution



def first_row_solution(constraints, list_of_rows):
    line_number = len(constraints[1])
    check_index = 0
    return check_row_and_line(check_index, constraints, line_number, [],
                              list_of_rows)



def compre_list(row_1, row_2):
    """ compere two list if value1 is -1 and value2 is 1 or 0 the function
    chage value1 to 1 or 0, the function return the number of -1 appeared in
     the valu1 and value2     """
    if row_1 == row_2:
        return row_2

    for i in range(len(row_1)):
        if row_1[i] != row_2[i]:

            if row_1[i] == -1:
                row_1[i] = row_2[i]
            elif row_2[i] == -1:
                continue
            else:
                print('there is a problem bro')  ###
                return
    return row_1


def first_line_solution(constraints, start_bord):
    """ its make reverse and if there isnt start bord, its make one  """
    rows_number = len(constraints[0])
    check_index = 1
    row_side_sol = make_list_of_index(start_bord)
    new_lines = check_row_and_line(check_index, constraints, rows_number, [], row_side_sol)
    line_result = make_list_of_index(new_lines)
    return line_result


def check_row_and_line(index, constraints, line_number, tmp_solution, start_row):  #
    """
    :param index:
    :param constraints:
    :param line_number:
    :param tmp_solution:
    :param start_row:
    :return: posibale option for bord by check the row
    """
    tmp_result = []
    for i, value in enumerate(constraints[index]):
        if not (bool(value)):  #############
            tmp_solution.append([0] * line_number) #########################################
            continue
        if len(value) == 1 and sum(value) == line_number:
            tmp_solution.append([1] * line_number)###########################################
            continue
        else:
            if type(start_row[0]) is list:
                tmp_result = get_row_variations(start_row[i], value) ####################
            if not type(start_row[0]) is list:
                tmp_result = get_row_variations([-1] * line_number, value)#################
            if len(tmp_result) == 1:
                tmp_solution.append(tmp_result[0])
                continue
            if len(tmp_result) > 1:
                the_best_option = get_intersection_row(
                    tmp_result)  ##### find from row_options the best option
                tmp_solution.append(the_best_option)
            else:
                tmp_solution.append([-1] * line_number)
    return tmp_solution


#####################################################################^3


# get_row_variations(row, blocks): #func 1 real
def solve_nonogram(constraints):  #### func 4
    option = []
    return solve_nonogram_helper4(constraints, option, [])

#
# def bro(constraints):
#     simple_result = solve_easy_nonogram(constraints)
#     rows_with_unknown = rows_with_unknown_check(simple_result)

def solve_nonogram_helper4(constraints, option, simple_result, num=0, first_enter = True):# helper func 4
    """
    :param constraints:
    :param option:
    :param simple_result:
    :param num:
    :param first_enter:
    :return:
    """
    if first_enter:
        simple_result = solve_easy_nonogram(constraints) ### משתמש בפונק' 3 ומוציא לוח
        first_enter = False
    if not simple_result: # מוודא שזה לא לוח ריק
        return
    list_of_index = rows_with_unknown_check(simple_result) # רשימה אינדקסים של השורות הבעייתיים

    if not list_of_index:
        if option:
            if check_if_results_same(option, simple_result):
                return
        return option.append(simple_result)

    index = list_of_index[num]
    if list_of_index:
        rows_option = get_row_variations(simple_result[index], constraints[0][index])

    for j in range(len(rows_option)):
        if -1 in rows_option[j] and rows_option[j][1:] == rows_option[j][:-1]: #   בדיקה אם הכל בשורה הוא -1 לא צריך לדעתי
            continue
        if rows_option[j] == simple_result[index]:
            continue
        simple_result[index] = rows_option[j]
        simple_result = check_row_and_line(0, constraints, len(constraints[1]), [], simple_result)
        solve_nonogram_helper4(constraints, option, simple_result,num, False)
        if j == len(rows_option) - 1 and index == list_of_index[-1]:
            return
    return option


def check_if_results_same(option, simple_result):##### למצוא דרך לייעל במהלך הבדיקה שהפונקציות זהות
    """return TRUE if same else return false"""

    for i in option:
        if i[0] == simple_result:
            return True
    return False



def rows_with_unknown_check(bord):
    """check if the bord contain -1
    :param bord: the list of list (the bord)
    :return: [] if the bord is full'
     else return list with the row index who contain -1"""
    rows_with_unknown = []
    if not bord:
        return
    for i, row in enumerate(bord):
        if -1 in row:
            rows_with_unknown.append(i)

    return rows_with_unknown


#############################################################^4
########################


def printer(x):
    for i in x:
        print()
        print(i)


####################

###########################
def len_checker(roows):
    x = len(roows[-1])
    for i in roows:
        if len(i) != x:
            print(False)
    print(True)


#########################


# my_constraints=[ [ [], [4], [6], [2, 2], [1, 3] ], [ [1,3], [2], [1], [2, 2], [2, 2]]]
# print(first_row_solution(
#     [[[1, 1, 1], [5], [3], [1], [5]], [[2, 1], [2, 1], [5], [2, 1], [2, 1]]]))

# printer(first_line_solution([[[1, 1, 1], [5], [3], [1], [5]], [[2, 1], [2, 1], [5], [2, 1], [2, 1]]]))

R = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [-1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1], [1, 1, 1, 1, 1]]
LL = [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [1, 1, 1, 1, 1],
      [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]

L = [[[1, 1, 1], [5], [3], [1], [5]],
     [[2, 1], [2, 1], [5], [2, 1], [2, 1]]]  # my_constraints

MY_DROW = [
    [[1], [1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [2, 1, 2], [1, 3, 1], [1, 1, 1],
     [7]],
    [[1], [5], [1, 1, 1], [1, 1, 1], [1, 6], [1, 1, 1], [1, 1, 1], [5], [1]]]

CON_FOR4 = [[[1], [1]], [[1], [1]]]

# print(get_row_variations([-1, -1], [1]))

# print(first_line_solution(L, R))
# printer(solve_easy_nonogram(MY_DROW))
# printer(R)
# print(0)
# printer(LL)

### 4444

AAA= [[1],[2],[2],[2],[1],[1]],[[2],[2],[2],[3]]
print(solve_nonogram(AAA))


#

######3333
# printer(solve_easy_nonogram(MY_DROW))
# len_checker(solve_easy_nonogram(MY_DROW))

 # func 1 tests
# print(1)
# print(get_row_variations([1,1,-1,0],[3]))
# print(2)
# print(get_row_variations([-1,-1,-1,0],[2]))
# print(3)
# print(get_row_variations([-1,0,1,0,-1,0],[1,1]))
# print(4)
# print(get_row_variations([-1,-1,-1],[1]))
# print(5)
# print(get_row_variations([0,0,0],[1]))
# print(6)
# print(get_row_variations([0,0,-1,1,0],[3]))
# print(7)
# print(get_row_variations([0,0,-1,1,0],[2]))
# print(8)
# print(get_row_variations([0,0,1,1,0],[2]))
# print(9)
# print(get_row_variations([-1,-1,-1,-1],[2,1]))

# print(compre_list(R[0], LL[0]))
# make_list_of_index([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(row_check([1,1], [2], 2, 3))
# print(get_intersection_row([[1, 0,1], [0, -1, 0]]))
# print(COUNT)
# print(check_for_get_row_variations([1, 0], [1, 1], 1))
# print(get_row_variations([[-1,-1,-1,-1,-1]], [1,3]))
# print(get_row_variations([1, 1, -1, 0], [3]))

# # # def add_one_queen(new_row, columns, prev_solutions):
# # #     return [solution + [new_column]
# # #             for solution in prev_solutions
# # #             for new_column in range(columns)
# # #             if no_conflict(new_row, new_column, solution)]
# # #
# # # def no_conflict(new_row, new_column, solution):
# # #     return all(solution[row]       != new_column           and
# # #                solution[row] + row != new_column + new_row and
# # #                solution[row] - row != new_column - new_row
# # #                for row in range(new_row))
# # #
# # # for solution in queensproblem(4, 4):
# # #     print(solution)
# # #
# # #     check_1 = (sum(blocks) - sum(tmp_lst) > len(row) - len(tmp_lst))
# # #     check_2 = (tmp_lst.count(1) > sum(blocks))
# # #     check_3 = (check_for_get_row_variations(tmp_lst, blocks, index))
# # #     if check_1 or check_2 or check_3:
# #
# #
# # x =[1,0,1]
# # y =[1,0,-1]
# #
# # import numpy
# # import matplotlib.pyplot as plt
# #
# # #גיבוי 6.1 14:05
# #
# #
# # COUNT = 0
# # BLACK = 1
# # WHITE = 0
# # UNKNOWN = -1
# #
# #
# # def helper_get_row_variations(row, blocks, tmp_lst, row_lst,
# #                               index):  # func 1 helper
# #     # global COUNT
# #     # print(index)
# #     lenght = len(row)
# #     # if sum(blocks) - sum(tmp_lst) > len(row) - len(tmp_lst):
# #     #     return
# #     if tmp_lst.count(1) > sum(blocks):
# #         return
# #     if index > 0 and not row_check(tmp_lst, blocks, index, lenght):
# #         return
# #     if len(tmp_lst) == lenght:
# #         if tmp_lst.count(1) != sum(blocks):
# #             return
# #         return row_lst.append(tmp_lst)
# #     # COUNT += 1
# #     if row[index] == UNKNOWN:
# #         tmp_lst.append(BLACK)
# #         helper_get_row_variations(row, blocks, tmp_lst[:], row_lst,
# #                                   index + 1)
# #         tmp_lst[-1] = WHITE
# #         helper_get_row_variations(row, blocks, tmp_lst[:], row_lst,
# #                                   index + 1)
# #     else:
# #         tmp_lst.append(row[index])
# #         helper_get_row_variations(row, blocks, tmp_lst[:], row_lst,
# #                                   index + 1)
# #     return row_lst
# #
# #
# # def row_check(tmp_lst, blocks, index, lenght):  # func 1
# #     """
# #     :return True if the checks is ok
# #     :param tmp_lst:
# #     :param blocks:
# #     :return:
# #     """
# #     counter = 0
# #     b_num = 0
# #     block_check = blocks[b_num]
# #     for i, v in enumerate(tmp_lst):
# #         if i != index - 1:
# #             if v == BLACK:
# #                 counter += 1
# #             if (v == BLACK) and (tmp_lst[i + 1] == 0):
# #                 if blocks[b_num] != counter:
# #                     return False
# #                 else:
# #                     counter = 0
# #                     b_num += 1
# #         else:
# #             if v == BLACK:
# #                 counter += 1
# #                 if blocks[b_num] != counter and not i < lenght - 1:  ##
# #                     return False
# #     return True
# #
# #
# # def get_row_variations(row, blocks):
# #     return helper_get_row_variations(row, blocks, [], [], 0)
# #
# #
# # def make_list_of_index(rows):
# #     lenght = len(rows[0])
# #     n = len(rows)
# #     tmp_lst = []
# #     list_of_index = []
# #     for i in range(lenght):  # line
# #         if i != 0:
# #             list_of_index.append(tmp_lst)
# #             tmp_lst = []
# #         for j in range(n):  # row external
# #             tmp_lst.append(rows[j][i])
# #     list_of_index.append(tmp_lst)
# #     return list_of_index
# #
# #
# # def get_intersection_row(rows):  # func 2
# #     """ recive list of list (option for one row) and return the option for
# #     the row
# #     i choose that this fun return inly what is 100% right"""
# #
# #     the_rows = make_list_of_index(rows)
# #     result = []
# #     for i in range(len(the_rows)):
# #         if all(x == the_rows[i][0] for x in the_rows[i]):
# #             result.append(the_rows[i][0])
# #             continue
# #         if 0 in the_rows[i] and (1 or -1) in the_rows[i]:
# #             result.append(-1)
# #             continue
# #         if (-1 and 1) in the_rows[i] and 0 not in the_rows[i]:
# #             if (the_rows[i].count(1)) // 2 >= the_rows[i].count(-1):
# #                 result.append(-1)  #### meantime
# #                 continue
# #             result.append(-1)
# #         else:
# #             result.append(-1)
# #     return result
# #
# #
# # def solve_easy_nonogram(constraints):  ## main
# #     """make the firs check and then cotinue to check if it not redey"""
# #     row_solution = first_row_solution(constraints, False)
# #     line_solution = first_line_solution(constraints, row_solution)
# #     # if row_solution == line_solution:
# #     #     return row_solution
# #     new_lst = []
# #     while row_solution != line_solution:
# #         new_lst = []
# #         for i in range(len(row_solution)):
# #             x = compre_list(row_solution[i], line_solution[i])
# #             new_lst.append(x)
# #         row_solution = first_row_solution(constraints, new_lst)
# #         line_solution = first_line_solution(constraints, row_solution)
# #     return new_lst
# #
# #
# # def compre_list(row_1, row_2):
# #     """ compere two list if value1 is -1 and value2 is 1 or 0 the function
# #     chage value1 to 1 or 0, the function return the number of -1 appeared in
# #      the valu1 and value2     """
# #     if row_1 == row_2:
# #         return row_2
# #     for i in range(len(row_1)):
# #         if row_1[i] != row_2[i]:
# #             if row_1[i] == -1:
# #                 row_1[i] = row_2[i]
# #             elif row_2[i] == -1:
# #                 continue
# #             else:
# #                 print('there is a problem bro')  ###
# #                 return
# #     return row_1
# #
# #
# # def first_line_solution(constraints, row_solution):
# #     """ its make reverse """
# #     rows_number = len(constraints[0])
# #     check_index = 1
# #     row_side_sol = make_list_of_index(row_solution)
# #
# #     new_lines = chack_row_and_line(check_index, constraints, rows_number, [],
# #                                    row_side_sol)
# #     line_result = make_list_of_index(new_lines)
# #     return line_result
# #
# #
# # def first_row_solution(constraints, line_side_solution=False):
# #     line_number = len(constraints[1])
# #     # tmp_solution = []
# #     if not line_side_solution:
# #         start_row = [-1] * line_number
# #         line_side_solution = start_row
# #     check_index = 0
# #     return chack_row_and_line(check_index, constraints, line_number, [],
# #                               line_side_solution)
# #
# #
# # def chack_row_and_line(index, constraints, line_number, tmp_solution,
# #                        start_row):
# #     for i, v in enumerate(constraints[index]):  #
# #         if not (bool(v)):  #############
# #             tmp_solution.append([0] * line_number)
# #             continue
# #         if len(v) == 1 and sum(v) == line_number:
# #             tmp_solution.append([1] * line_number)
# #             continue
# #         else:
# #             if type(start_row[0]) is list:
# #                 tmp_result = get_row_variations(start_row[i], v)
# #             if not type(start_row[0]) is list:
# #                 tmp_result = get_row_variations([-1] * line_number, v)
# #             if len(tmp_result) == 1:
# #                 tmp_solution.append(tmp_result[0])
# #                 continue
# #             if len(tmp_result) > 1:
# #                 x = get_intersection_row(
# #                     tmp_result)  ##### find from row_options the best option
# #                 tmp_solution.append(x)
# #             else:
# #                 tmp_solution.append([-1] * line_number)
# #     return tmp_solution
# #
# #
# # ########################
# # def printer(x):
# #     for i in x:
# #         print(i)
# #
# #
# # ####################
# #
# # ###########################
# # def len_checker(roows):
# #     x = len(roows[-1])
# #     for i in roows:
# #         if len(i) != x:
# #             return False
# #     return True
# #
# #
# # #########################
# #
# #
# # # my_constraints=[ [ [], [4], [6], [2, 2], [1, 3] ], [ [1,3], [2], [1], [2, 2], [2, 2]]]
# # # print(first_row_solution(
# # #     [[[1, 1, 1], [5], [3], [1], [5]], [[2, 1], [2, 1], [5], [2, 1], [2, 1]]]))
# #
# # # printer(first_line_solution([[[1, 1, 1], [5], [3], [1], [5]], [[2, 1], [2, 1], [5], [2, 1], [2, 1]]]))
# #
# # R = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [-1, -1, -1, -1, -1],
# #      [-1, -1, -1, -1, -1], [1, 1, 1, 1, 1]]
# # LL = [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [1, 1, 1, 1, 1],
# #       [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]
# #
# # L = [[[1, 1, 1], [5], [3], [1], [5]],
# #      [[2, 1], [2, 1], [5], [2, 1], [2, 1]]]  # my_constraints
# #
# # MY_DROW = [
# #     [[1], [1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [2, 1, 2], [1, 3, 1], [1, 1, 1],
# #      [7]],
# #     [[1], [5], [1, 1, 1], [1, 1, 1], [1, 6], [1, 1, 1], [1, 1, 1], [5], [1]]]
# #
# # # print(first_line_solution(L, R))
# # printer(solve_easy_nonogram(MY_DROW))
# # # printer(R)
# # # print()
# # # printer(LL)
# #
# #
# # # print(len_checker(solve_easy_nonogram(MY_DROW)))
# #
# # # print(compre_list(R[0], LL[0]))
# # # make_list_of_index([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# #
# #
# # # print(get_intersection_row([[0, 1, -1], [-1, -1, -1]]))
# # # print(COUNT)
# # # print(check_for_get_row_variations([1, 0], [1, 1], 1))
# # # print(get_row_variations([[-1,-1,-1,-1,-1]], [1,3]))
# #
# #
# #
# # # אחד אחר של זה
# #
# # # def chack_row_and_line(index, constraints, line_number, tmp_solution,start_row):#
# # #     for i, value in enumerate(constraints[index]):
# # #         if not (bool(value)):  #############
# # #             tmp_solution.append([0] * line_number)
# # #             continue
# # #         if len(value) == 1 and sum(value) == line_number:
# # #             tmp_solution.append([1] * line_number)
# # #             continue
# # #         else:
# # #             # if type(start_row[0]) is list:
# # #             tmp_result = get_row_variations(start_row[i], value)
# # #             # if not type(start_row[0]) is list:
# # #             #     tmp_result = get_row_variations([-1] * line_number, value)
# # #             if len(tmp_result) == 1:
# # #                 tmp_solution.append(tmp_result[0])
# # #                 continue
# # #             if len(tmp_result) > 1:
# # #                 the_best_option = get_intersection_row(tmp_result)  ##### find from row_options the best option
# # #                 tmp_solution.append(the_best_option)
# # #             else:
# # #                 tmp_solution.append([-1] * line_number)
# # #     return tmp_solution
# #
# # #5:04 לפני שינוי שורות ועמודות בפפונקציה 3
# # COUNT = 0
# # BLACK = 1
# # WHITE = 0
# # UNKNOWN = -1
# #
# #
# # def helper_get_row_variations(row, blocks, tmp_lst, row_lst,
# #                               index):  # func 1 helper
# #     # global COUNT
# #     # print(index)
# #     lenght = len(row)
# #     # if sum(blocks) - sum(tmp_lst) > len(row) - len(tmp_lst):
# #     #     return
# #     if tmp_lst.count(1) > sum(blocks):
# #         return
# #     if index > 0 and not row_check(tmp_lst, blocks, index, lenght):
# #         return
# #     if len(tmp_lst) == lenght:
# #         if tmp_lst.count(1) != sum(blocks):
# #             return
# #         return row_lst.append(tmp_lst)
# #     # COUNT += 1
# #     if row[index] == UNKNOWN:
# #         tmp_lst.append(BLACK)
# #         helper_get_row_variations(row, blocks, tmp_lst[:], row_lst,
# #                                   index + 1)
# #         tmp_lst[-1] = WHITE
# #         helper_get_row_variations(row, blocks, tmp_lst[:], row_lst,
# #                                   index + 1)
# #     else:
# #         tmp_lst.append(row[index])
# #         helper_get_row_variations(row, blocks, tmp_lst[:], row_lst,
# #                                   index + 1)
# #     return row_lst
# #
# #
# # def row_check(tmp_lst, blocks, index, lenght):  # func 1
# #     """
# #     :return True if the checks is ok
# #     :param tmp_lst:
# #     :param blocks:
# #     :return:
# #     """
# #     counter = 0
# #     b_num = 0
# #     block_check = blocks[b_num]
# #     for i, v in enumerate(tmp_lst):
# #         if i != index - 1:
# #             if v == BLACK:
# #                 counter += 1
# #             if (v == BLACK) and (tmp_lst[i + 1] == 0):
# #                 if blocks[b_num] != counter:
# #                     return False
# #                 else:
# #                     counter = 0
# #                     b_num += 1
# #         else:
# #             if v == BLACK:
# #                 counter += 1
# #                 if blocks[b_num] != counter and not i < lenght - 1:  ##
# #                     return False
# #     return True
# #
# #
# # def get_row_variations(row, blocks):  # func 1 real
# #     return helper_get_row_variations(row, blocks, [], [], 0)
# #
# #
# # ####################################################################^1
# #
# # def make_list_of_index(rows):
# #     lenght = len(rows[0])
# #     n = len(rows)
# #     tmp_lst = []
# #     list_of_index = []
# #     for i in range(lenght):  # line
# #         if i != 0:
# #             list_of_index.append(tmp_lst)
# #             tmp_lst = []
# #         for j in range(n):  # row external
# #             tmp_lst.append(rows[j][i])
# #     list_of_index.append(tmp_lst)
# #     return list_of_index
# #
# #
# # def get_intersection_row(rows):  # func 2
# #     """ recive list of list (option for one row) and return the option for
# #     the row
# #     i choose that this fun return inly what is 100% right"""
# #
# #     the_rows = make_list_of_index(rows)
# #     result = []
# #     for i in range(len(the_rows)):
# #         if all(x == the_rows[i][0] for x in the_rows[i]):
# #             result.append(the_rows[i][0])
# #             continue
# #         if 0 in the_rows[i] and (1 or -1) in the_rows[i]:
# #             result.append(-1)
# #             continue
# #         if (-1 and 1) in the_rows[i] and 0 not in the_rows[i]:
# #             if (the_rows[i].count(1)) // 2 >= the_rows[i].count(-1):
# #                 result.append(-1)  #### meantime
# #                 continue
# #             result.append(-1)
# #         else:
# #             result.append(-1)
# #     return result
# #
# #
# # #########################################################################^2
# #
# #
# # def solve_easy_nonogram(constraints):  ## main
# #     """make the firs check and then cotinue to check if it not redey"""
# #     row_solution = first_row_solution(constraints, [])
# #     line_solution = first_line_solution(constraints, row_solution)
# #     # if row_solution == line_solution:
# #     #     return row_solution
# #     new_lst = []
# #     while row_solution != line_solution:
# #         new_lst = []
# #         for i in range(len(row_solution)):
# #             x = compre_list(row_solution[i], line_solution[i])
# #             new_lst.append(x)
# #         row_solution = first_row_solution(constraints, new_lst)
# #         line_solution = first_line_solution(constraints, row_solution)
# #
# #     return line_solution
# #
# #
# # def first_row_solution(constraints, list_of_rows):
# #     line_number = len(constraints[1])
# #     if not list_of_rows:
# #         start_row = [-1] * line_number
# #         list_of_rows = start_row
# #     check_index = 0
# #     return check_row_and_line(check_index, constraints, line_number, [],
# #                               list_of_rows)
# #
# #
# # def compre_list(row_1, row_2):
# #     """ compere two list if value1 is -1 and value2 is 1 or 0 the function
# #     chage value1 to 1 or 0, the function return the number of -1 appeared in
# #      the valu1 and value2     """
# #     if row_1 == row_2:
# #         return row_2
# #     for i in range(len(row_1)):
# #         if row_1[i] != row_2[i]:
# #             if row_1[i] == -1:
# #                 row_1[i] = row_2[i]
# #             elif row_2[i] == -1:
# #                 continue
# #             else:
# #                 print('there is a problem bro')  ###
# #                 return
# #     return row_1
# #
# #
# # def first_line_solution(constraints, row_solution):
# #     """ its make reverse """
# #     rows_number = len(constraints[0])
# #     check_index = 1
# #     row_side_sol = make_list_of_index(row_solution)
# #
# #     new_lines = check_row_and_line(check_index, constraints, rows_number, [],
# #                                    row_side_sol)
# #     line_result = make_list_of_index(new_lines)
# #     return line_result
# #
# #
# # def check_row_and_line(index, constraints, line_number, tmp_solution,
# #                        start_row):  #
# #     tmp_result = []
# #     for i, value in enumerate(constraints[index]):
# #         if not (bool(value)):  #############
# #             tmp_solution.append([0] * line_number)
# #             continue
# #         if len(value) == 1 and sum(value) == line_number:
# #             tmp_solution.append([1] * line_number)
# #             continue
# #         else:
# #             if type(start_row[0]) is list:
# #                 tmp_result = get_row_variations(start_row[i], value)
# #             if not type(start_row[0]) is list:
# #                 tmp_result = get_row_variations([-1] * line_number, value)
# #             if len(tmp_result) == 1:
# #                 tmp_solution.append(tmp_result[0])
# #                 continue
# #             if len(tmp_result) > 1:
# #                 the_best_option = get_intersection_row(
# #                     tmp_result)  ##### find from row_options the best option
# #                 tmp_solution.append(the_best_option)
# #             else:
# #                 tmp_solution.append([-1] * line_number)
# #     return tmp_solution
# #
# #
# # #####################################################################^3
# #
# # # get_row_variations(row, blocks): #func 1 real
# # def solve_nonogram(constraints):  #### func 4
# #     pass
# #
# #
# # def solve_nonogram_helper4(constraints):  # helper func 4
# #     simple_result = solve_easy_nonogram(constraints)
# #     rows_with_unknown = rows_with_unknown_check(simple_result)
# #     if rows_with_unknown:
# #         for i in rows_with_unknown:
# #             simple_result[i] =
# #             solve_easy_nonogram(constraints)
# #
# #
# #
# #
# #
# #     else:
# #         return simple_result
# #
# #
# # def rows_with_unknown_check(bord):
# #     """check if the bord contain -1
# #     :param bord: the list of list (the bord)
# #     :return: [] if the bord is full'
# #      else return list with the row index who contain -1"""
# #     rows_with_unknown = []
# #     for i, row in enumerate(bord):
# #         if -1 in row:
# #             rows_with_unknown.append(i)
# #     return rows_with_unknown
# #
# #
# # #############################################################^4
# # ########################
# #
# #
# # def printer(x):
# #     for i in x:
# #         print(i)
# #
# #
# # ####################
# #
# # ###########################
# # def len_checker(roows):
# #     x = len(roows[-1])
# #     for i in roows:
# #         if len(i) != x:
# #             return False
# #     return True
# #
# #
# # #########################
# #
# #
# # # my_constraints=[ [ [], [4], [6], [2, 2], [1, 3] ], [ [1,3], [2], [1], [2, 2], [2, 2]]]
# # # print(first_row_solution(
# # #     [[[1, 1, 1], [5], [3], [1], [5]], [[2, 1], [2, 1], [5], [2, 1], [2, 1]]]))
# #
# # # printer(first_line_solution([[[1, 1, 1], [5], [3], [1], [5]], [[2, 1], [2, 1], [5], [2, 1], [2, 1]]]))
# #
# # R = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [-1, -1, -1, -1, -1],
# #      [-1, -1, -1, -1, -1], [1, 1, 1, 1, 1]]
# # LL = [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [1, 1, 1, 1, 1],
# #       [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]
# #
# # L = [[[1, 1, 1], [5], [3], [1], [5]],
# #      [[2, 1], [2, 1], [5], [2, 1], [2, 1]]]  # my_constraints
# #
# # MY_DROW = [
# #     [[1], [1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [2, 1, 2], [1, 3, 1], [1, 1, 1],
# #      [7]],
# #     [[1], [5], [1, 1, 1], [1, 1, 1], [1, 6], [1, 1, 1], [1, 1, 1], [5], [1]]]
# #
# # CON_FOR4 = [[[1], [1]], [[1], [1]]]
# #
# # print(get_row_variations([-1, -1], [1]))
# #
# # # print(first_line_solution(L, R))
# # # printer(solve_easy_nonogram(CON_FOR4))
# # # printer(R)
# # # print()
# # # printer(LL)
# #
# #
# # # print(len_checker(solve_easy_nonogram(MY_DROW)))
# #
# # # print(compre_list(R[0], LL[0]))
# # # make_list_of_index([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# #
# #
# # # print(get_intersection_row([[0, 1, -1], [-1, -1, -1]]))
# # # print(COUNT)
# # # print(check_for_get_row_variations([1, 0], [1, 1], 1))
# # # print(get_row_variations([[-1,-1,-1,-1,-1]], [1,3]))
#
#
# def solve_nonogram_helper4(constraints, option, lst):  # helper func 4
#     simple_result = helper_func3(constraints,
#                                  lst)  ### משתמש בפונק' 3 ומוציא לוח
#
#     if not simple_result:  # מוודא שזה לא לוח ריק
#         return
#     rows_with_unknown_indexs = rows_with_unknown_check(
#         simple_result)  # רשימה אינדקסים של השורות הבעייתיים
#     if not rows_with_unknown_indexs:
#         return option.append(simple_result)
#
#     if rows_with_unknown_indexs:
#
#         for i in rows_with_unknown_indexs:
#             rows_option = get_row_variations(simple_result[i],
#                                              constraints[0][i])
#
#             for j in range(len(rows_option)):
#                 if -1 in rows_option[j] and rows_option[j][1:] == rows_option[
#                                                                       j][:-1]:
#                     continue
#                 if rows_option[j] == simple_result[i]:
#                     continue
#                 simple_result[i] = rows_option[j]
#                 solve_nonogram_helper4(constraints, simple_result, option)
#                 if j == len(rows_option) - 1 and i == rows_with_unknown_indexs[
#                     -1]:
#                     return
#     else:
#         return simple_result

COUNT = 0
BLACK = 1
WHITE = 0
UNKNOWN = -1

import math


#################################### יעילות לפי אורך שורה


def helper_get_row_variations(row, blocks, tmp_lst, row_lst,
                              index):  # func 1 helper
    global COUNT
    # print(index)
    lenght = len(row)

    if index == 0:
        found_common_cases = common_cases(row, blocks)
        if found_common_cases:
            answer = get_intersection_row([row, found_common_cases])
            if not rows_with_unknown_check([answer]):
                return [found_common_cases]

    if sum(blocks) - sum(tmp_lst) > len(row) - len(tmp_lst):
        return
    if tmp_lst.count(BLACK) > sum(blocks):
        return
    if index > 1 and not row_check(tmp_lst, blocks, index, lenght):
        return
    if len(tmp_lst) == lenght:
        if tmp_lst.count(BLACK) != sum(blocks):
            return
        return row_lst.append(tmp_lst)
    COUNT += 1
    if row[index] == UNKNOWN:
        tmp_lst.append(BLACK)
        helper_get_row_variations(row, blocks, tmp_lst[:], row_lst, index + 1)
        tmp_lst[-1] = WHITE
        helper_get_row_variations(row, blocks, tmp_lst[:], row_lst, index + 1)
    else:
        tmp_lst.append(row[index])
        helper_get_row_variations(row, blocks, tmp_lst[:], row_lst, index + 1)
    return row_lst


def common_cases(row, block):
    row_long = len(row)
    num_of_black = sum(block)
    block_length = len(block)
    lst = []
    if num_of_black + len(
            block) - 1 == row_long:  #################################
        for i, value in enumerate(block):
            lst.extend([BLACK] * value)
            if i != block_length - 1:
                lst.append(WHITE)
        return lst
    if not block:  ### zero row
        return lst.extend([WHITE] * row_long)
    if num_of_black == row_long:  ## all black
        return lst.extend([BLACK] * row_long)

    # if sum(blocks) = le###    all black option


def row_check(tmp_lst, blocks, index, lenght):  # func 1
    """
    :return True if the checks is ok
    :param tmp_lst:
    :param blocks:
    :return:
    """
    counter = 0
    b_num = 0
    block_check = blocks[b_num]
    # print('row_check')
    for i, v in enumerate(tmp_lst):
        if i != index - 1:  # check if first?
            if v == BLACK:
                counter += 1
                if tmp_lst[i + 1] == 0:
                    if blocks[b_num] != counter:
                        return False
                    else:
                        counter = 0
                        b_num += 1
        else:
            if v == BLACK:
                counter += 1
                if blocks[b_num] != counter and not i < lenght - 1:  ##
                    return False
    return True


def get_row_variations(row, blocks):  # func 1 real
    return helper_get_row_variations(row, blocks, [], [], 0)


####################################################################^1

def make_list_of_index(rows):
    lenght = len(rows[0])
    n = len(rows)
    tmp_lst = []
    list_of_index = []
    for i in range(lenght):  # line
        if i != 0:
            list_of_index.append(tmp_lst)
            tmp_lst = []
        for j in range(n):  # row external
            tmp_lst.append(rows[j][i])
    list_of_index.append(tmp_lst)
    return list_of_index


def get_intersection_row(rows):  # func 2
    """ recive list of list (option for one row) and return the option for
    the row
    i choose that this func return only what is 100% right"""

    the_rows = make_list_of_index(rows)
    result = []
    for i in range(len(the_rows)):
        if all(x == the_rows[i][0] for x in the_rows[i]):  ###
            result.append(the_rows[i][0])
            continue
        if 0 in the_rows[i] and (1 or -1) in the_rows[i]:
            result.append(UNKNOWN)
            continue
        if (-1 and 1) in the_rows[i] and 0 not in the_rows[i]:
            if (the_rows[i].count(1)) // 2 >= the_rows[i].count(-1):
                result.append(UNKNOWN)  #### meantime
                continue
            result.append(UNKNOWN)
        else:
            result.append(UNKNOWN)
    return result


#########################################################################^2

############################################################################

def solve_easy_nonogram(constraints):  ## main
    """make the firs check and then cotinue to check if it not redey"""
    # empty_list = []
    bord = find_start_bord(constraints)
    return helper_func3(constraints, bord)


def find_start_bord(constraints):
    """
    make mat
    :param constraints:
    :return:
    """
    line_num = len(constraints[1])
    row_num = len(constraints[0])
    first_bord = []
    for i in range(row_num):
        tmp = []
        tmp.extend([UNKNOWN] * line_num)
        first_bord.append(tmp)
    return first_bord


def helper_func3(constraints, start_bord):
    line_solution = first_line_solution(constraints, start_bord)
    row_solution = first_row_solution(constraints, line_solution)
    if row_solution == line_solution:
        return row_solution
    new_lst = []
    make_2_check_loops = 2

    while make_2_check_loops:
        # printer(line_solution)
        new_lst = []  ################################################################## פה
        for i in range(len(row_solution)):
            x = compre_list(row_solution[i], line_solution[i])
            new_lst.append(x)
        row_solution = first_row_solution(constraints, new_lst)
        line_solution = first_line_solution(constraints, row_solution)
        # print('ofir the king')
        if row_solution != line_solution:
            make_2_check_loops = 2
        else:
            if make_2_check_loops == 0:
                print('out')
                break
            make_2_check_loops -= 1

    return line_solution


def first_row_solution(constraints, list_of_rows):
    line_number = len(constraints[1])
    check_index = 0
    return check_row_and_line(check_index, constraints, line_number, [],
                              list_of_rows)


def compre_list(row_1, row_2):
    """ compere two list if value1 is -1 and value2 is 1 or 0 the function
    chage value1 to 1 or 0, the function return the number of -1 appeared in
     the valu1 and value2     """
    if row_1 == row_2:
        return row_2

    for i in range(len(row_1)):
        if row_1[i] != row_2[i]:

            if row_1[i] == -1:
                row_1[i] = row_2[i]
            elif row_2[i] == -1:
                continue
            else:
                # print('there is a problem bro')  ###
                return
    return row_1


def first_line_solution(constraints, start_bord):
    """ its make reverse and if there isnt start bord, its make one  """
    rows_number = len(constraints[0])
    check_index = 1
    row_side_sol = make_list_of_index(start_bord)
    new_lines = check_row_and_line(check_index, constraints, rows_number, [],
                                   row_side_sol)
    line_result = make_list_of_index(new_lines)
    return line_result


def check_row_and_line(index, constraints, line_number, tmp_solution,
                       start_row):  #
    """
    :param index:
    :param constraints:
    :param line_number:
    :param tmp_solution:
    :param start_row:
    :return: posibale option for bord by check the row
    """
    tmp_result = []
    for i, value in enumerate(constraints[index]):
        if not (bool(value)):  #############
            tmp_solution.append([
                                    WHITE] * line_number)  #########################################
            continue
        if len(value) == 1 and sum(value) == line_number:
            tmp_solution.append([
                                    BLACK] * line_number)  ###########################################
            continue
        else:
            if type(start_row[0]) is list:
                tmp_result = get_row_variations(start_row[i],
                                                value)  ####################
            if not type(start_row[0]) is list:
                tmp_result = get_row_variations([-1] * line_number,
                                                value)  #################
            if len(tmp_result) == 1:
                tmp_solution.append(tmp_result[0])
                continue
            if len(tmp_result) > 1:
                the_best_option = get_intersection_row(
                    tmp_result)  ##### find from row_options the best option
                tmp_solution.append(the_best_option)
            else:
                tmp_solution.append([UNKNOWN] * line_number)
    return tmp_solution


#####################################################################^3


# get_row_variations(row, blocks): #func 1 real
def solve_nonogram(constraints):  #### func 4
    option = []
    return solve_nonogram_helper4(constraints, option, [])


#
# def bro(constraints):
#     simple_result = solve_easy_nonogram(constraints)
#     rows_with_unknown = rows_with_unknown_check(simple_result)

def solve_nonogram_helper4(constraints, option, simple_result, num=0,
                           first_enter=True):  # helper func 4
    """
    :param constraints:
    :param option:
    :param simple_result:
    :param num:
    :param first_enter:
    :return:
    """
    if first_enter:
        simple_result = solve_easy_nonogram(
            constraints)  ### משתמש בפונק' 3 ומוציא לוח
        first_enter = False
    if not simple_result:  # מוודא שזה לא לוח ריק
        return
    list_of_index = rows_with_unknown_check(
        simple_result)  # רשימה אינדקסים של השורות הבעייתיים

    if not list_of_index:
        if option:
            if check_if_results_same(option, simple_result):
                return
        return option.append(simple_result)

    index = list_of_index[num]
    if list_of_index:
        rows_option = get_row_variations(simple_result[index],
                                         constraints[0][index])

    for j in range(len(
            rows_option)):  ###########################################################################################
        if UNKNOWN in rows_option[j] and rows_option[j][1:] == rows_option[j][
                                                               :-1]:  # בדיקה אם הכל בשורה הוא -1 לא צריך לדעתי
            continue
        if rows_option[j] == simple_result[index]:
            continue
        simple_result[index] = rows_option[j]
        simple_result = check_row_and_line(0, constraints, len(constraints[1]),
                                           [], simple_result)
        solve_nonogram_helper4(constraints, option, simple_result, num, False)
        if j == len(rows_option) - 1 and index == list_of_index[-1]:
            return
    return option


def check_if_results_same(option,
                          simple_result):  ##### למצוא דרך לייעל במהלך הבדיקה שהפונקציות זהות
    """return TRUE if same else return false"""

    for i in option:
        if i == simple_result:
            return True
    return False


def rows_with_unknown_check(bord):
    """check if the bord contain -1
    :param bord: the list of list (the bord)
    :return: [] if the bord is full'
     else return list with the row index who contain -1"""
    rows_with_unknown = []
    if not bord:
        return
    for i, row in enumerate(bord):
        if UNKNOWN in row:
            rows_with_unknown.append(i)

    return rows_with_unknown


#############################################################^4
########################
def count_row_variations(length, blocks):
    num_block = len(blocks)
    the_amount_of_black = sum(blocks)
    if the_amount_of_black >= length - (
            num_block - 1):  #### if there isnt inaf place
        return 0
    k = length - the_amount_of_black - (num_block - 1)
    n = length - the_amount_of_black + 1
    return int(binom_n_k(n, k))


def binom_n_k(n, k):
    f = math.factorial
    return f(n) / f(k) / f(n - k)


def countt_row_variation(length, blocks):  ################ למחוק
    x = get_row_variations(length * [-1], blocks)
    y = len(x)
    for i in x:
        print(i)
    print(y)
    return x


# countt_row_variation(40, [2,2,2,2,2])

print(count_row_variations(1, [2]))

############################################################^555555


WHITE_BLANK_REP = 0
BLACK_BLANK_REP = 1
WHITE_BLANK = "_"
BLACK_BLANK = "X"
UNKNOWN_BLANK = "?"
CHR_SEPARATOR = " "
LINE_REGEX = "(?:[1]*)"
LINE_SEPARATOR = " "
REPLACE_FROM = "-1"
REPLACE_TO = "0"


def print_board(board):
    """
    This function prints the input board game to the screen.
    :param board: The matrix that represents the game board.
    :return: None
    """
    rep_str = ""
    for row in board:
        for blank in row:
            if blank == WHITE_BLANK_REP:
                rep_str += WHITE_BLANK
            elif blank == BLACK_BLANK_REP:
                rep_str += BLACK_BLANK
            else:
                rep_str += UNKNOWN_BLANK
            rep_str += CHR_SEPARATOR
        rep_str += "\n"
    print(rep_str)


###############################
def printer(x):
    for i in x:
        print()
        print(i)


####################

###########################
def len_checker(roows):
    x = len(roows[-1])
    for i in roows:
        if len(i) != x:
            print(False)
    print(True)


#########################

def fine_if_equal(AAAA):
    for i in AAAA:
        if i == AAAA[-1]:
            print('problem menn')


# my_constraints=[ [ [], [4], [6], [2, 2], [1, 3] ], [ [1,3], [2], [1], [2, 2], [2, 2]]]
# print(first_row_solution(
#     [[[1, 1, 1], [5], [3], [1], [5]], [[2, 1], [2, 1], [5], [2, 1], [2, 1]]]))

# printer(first_line_solution([[[1, 1, 1], [5], [3], [1], [5]], [[2, 1], [2, 1], [5], [2, 1], [2, 1]]]))

R = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [-1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1], [1, 1, 1, 1, 1]]
LL = [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [1, 1, 1, 1, 1],
      [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]

L = [[[1, 1, 1], [5], [3], [1], [5]],
     [[2, 1], [2, 1], [5], [2, 1], [2, 1]]]  # my_constraints

MY_DROW = [
    [[1], [1, 1], [1, 1, 1, 1, 1], [1, 1, 1], [2, 1, 2], [1, 3, 1], [1, 1, 1],
     [7]],
    [[1], [5], [1, 1, 1], [1, 1, 1], [1, 6], [1, 1, 1], [1, 1, 1], [5], [1]]]

CON_FOR4 = [[[1], [1]], [[1], [1]]]

# print(get_row_variations([-1, -1], [1]))

# print(first_line_solution(L, R))
# printer(solve_easy_nonogram(MY_DROW))
# printer(R)
# print(0)
# printer(LL)


###################################          4444444444444444444444444

AAA = [[1], [2], [2], [2], [1], [1]], [[2], [2], [2], [3]]
# printer(solve_nonogram(AAA))

# AAAA = solve_nonogram(AAA)
# fine_if_equal(AAAA)
# print(COUNT)

######3333
# print_board(solve_easy_nonogram(MY_DROW))
# len_checker(solve_easy_nonogram(MY_DROW))

# func 1 tests
# print(1)
# print(get_row_variations([1,1,-1,0],[3]))
# print(2)
# print(get_row_variations([-1,-1,-1,0],[2]))
# print(3)
# print(get_row_variations([-1,0,1,0,-1,0],[1,1]))
# print(4)
# print(get_row_variations([-1,-1,-1],[1]))
# print(5)
# print(get_row_variations([0,0,0],[1]))
# print(6)
# print(get_row_variations([0,0,-1,1,0],[3]))
# print(7)
# print(get_row_variations([0,0,-1,1,0],[2]))
# print(8)
# print(get_row_variations([0,0,1,1,0],[2]))
# print(9)
# print(get_row_variations([-1,-1,-1,-1],[2,1]))

# print(compre_list(R[0], LL[0]))
# make_list_of_index([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(row_check([1,1], [2], 2, 3))
# print(get_intersection_row([[1, 0,1], [0, -1, 0]]))

# print(check_for_get_row_variations([1, 0], [1, 1], 1))
# print(get_row_variations([[-1,-1,-1,-1,-1]], [1,3]))
# print(get_row_variations([1, 1, -1, 0], [3]))









