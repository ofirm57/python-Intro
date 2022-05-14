#################################################################
# FILE : ex3.py
# WRITER :ofir  , ofirm57 , 205660731
# EXERCISE : intro2cs2 ex 2020
# DESCRIPTION:
#################################################################

def input_list():
    """function that receives input of numbers (in strings).
    And takes out an output list of all The numbers
     entered (as a numeric value) and at the last place in the
    list are added the sum of the input numbers """

    user_input = input()
    output = []
    user_input = user_input.split()
    su_m = 0

    for i in range(len(user_input)):
        t = float(user_input[i])
        output.append(t)
        su_m += float(user_input[i])

    output.append(su_m)

    return output


def inner_product(vec_1, vec_2):
    """ צריך לכתוב תיאור יא מלך """
    total = 0
    # lst = []
    if len(vec_1) == len(vec_2):

        for i in range(len(vec_1)):
            tmp_sum = vec_1[i] * vec_2[i]
            total += tmp_sum

        return total

    else:
        return None


# print(inner_product([], []))

def sequence_monotonicity(sequence=list):
    """ תיאור  """
    lst = []
    tmp0 = 1
    tmp1 = 1
    tmp2 = 1
    tmp3 = 1

    for i in range(1, len(sequence)):

        if sequence[i] > sequence[i - 1]:
            tmp0 *= True
        else:
            tmp0 *= False

        if sequence[i] >= sequence[i - 1]:
            tmp1 *= True
        else:
            tmp1 *= False

        if sequence[i] < sequence[i - 1]:
            tmp2 *= True
        else:
            tmp2 *= False

        if sequence[i] <= sequence[i - 1]:
            tmp3 *= True
        else:
            tmp3 *= False

    lst.append(bool(tmp0))
    lst.append(bool(tmp1))
    lst.append(bool(tmp2))
    lst.append(bool(tmp3))

    return lst


# print(sequence_monotonicity([1, 1, 1, 1]))


def monotonicity_inverse(def_bool):

"""אין פה לולאות """

    if def_bool[1] and def_bool[2]:
        return [0, 0, 0, 0]

    if def_bool[0]:
        return [1, 2, 3, 4]

    if def_bool[1]:
        return [1, 1, 3, 3]

    if def_bool[2]:
        return [4, 3, 2, 1]

    if def_bool[3]:
        return [4, 4, -1, -1]

    else:
        return [-100, 0, 100, 5]


print(monotonicity_inverse([False, False, False, False]))


def primes_for_asafi(n): 