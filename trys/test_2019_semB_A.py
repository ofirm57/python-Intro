##########################################################
#            Tester for 2019 SemesterB - A              #
########################################################
# Run with pytest. Change the file imported from.     #
# Questions tested:                                  #
#       - 2A (using 2B)                             #
#       - 2B                                       #
#       - 4                                       #
#       - 5                                      #
#       - 6                                     #
# Using mainly the examples from the test form.#
#                                             #
#    Roy 'HaPatish' Urbach                   #
#############################################

from trys import*  # write the answers' filename here


#   ~ 2nd Question ~

def test_describe_str():
    f2a = describe_str
    assert f2a('abbcccdeaa') == 'a1b2c3d1e1a2'
    assert f2a('aaabbbccc') == 'a3b3c3'
    assert f2a('aba') == 'a1b1a1'
    assert f2a('') == ''
    assert f2a('1234a1234') == '11213141a111213141'


def test_same_char_helper():
    f2b = same_char_helper
    string1 = 'aabbbcccccdd'
    string2 = 'ab11 aa'
    assert f2b(string1, 0) == 2
    assert f2b(string1, 4) == 1
    assert f2b(string1, 5) == 5
    assert f2b(string1, 5) == 5
    assert f2b(string2, 0) == 1
    assert f2b(string2, 1) == 1
    assert f2b(string2, 2) == 2
    assert f2b(string2, 3) == 1
    assert f2b(string2, 4) == 1
    assert f2b(string2, 5) == 2
    assert f2b(string2, 6) == 1


#   ~ 4th Question ~

class Child:
    def __init__(self, name, mother, father):
        self.name = name
        self.mother = mother
        self.father = father


x = Child('Ety', None, None)
y = Child('Malka', x, None)
z = Child('Iosi', y, x)
u = Child('Ely', z, None)
v = Child('Avi', None, None)


def test_family_tree():
    f4 = family_tree
    assert f4(u,x) is True
    assert f4(x,x) is True
    assert f4(v,x) is False


#   ~ 5th Question ~

def test_rev_list():
    f5a = rev_list_rec
    assert f5a(['a', 'b', 3, 5, [1, 2]]) == [[1, 2], 5, 3, 'b', 'a']
    assert f5a([1, 2, 3]) == [3, 2, 1]
    assert f5a([(2, 3, 4), 1, [15, 10]]) == [[15, 10], 1, (2, 3, 4)]
    assert f5a(['a', {1: 2}, 0, 0, 0]) == [0, 0, 0, {1: 2}, 'a']
    assert f5a([]) == []


def test_list_rec():
    f5b = list_rec
    assert f5b(['a', 'b', 3, 5, [1, 2]]) == [[1, 2], 5, 3, 'b', 'a']
    assert f5b([1,2,3]) == [3,2,1]
    assert f5b([(2,3,4), 1, [15,10]]) == [[15,10], 1, (2,3,4)]
    assert f5b(['a', {1: 2}, 0, 0, 0]) == [0, 0, 0, {1:2}, 'a']
    assert f5b([]) == []


#   ~ 6th Question ~

def test_mat_gen():
    f6 = mat_gen

    # even number of steps
    matrix1 = [[1, 2, 3, 4], [2, 8, 6, 4], [5, 1, 7, 9]]
    tester1 = f6()(matrix1)
    assert next(tester1) == [1, 2, 3, 4]
    assert matrix1 == [[2, 8, 6, 4], [5, 1, 7, 9]]
    assert next(tester1) == [2, 5]
    assert matrix1 == [[8, 6, 4], [1, 7, 9]]
    assert next(tester1) == [8, 6, 4]
    assert matrix1 == [[1, 7, 9]]
    assert next(tester1) == [1]
    assert matrix1 == [[7, 9]]
    assert next(tester1) == [7, 9]
    assert matrix1 == []
    assert mat_gen_helper(tester1)

    # odd number of steps
    matrix2 = [[1, 2], [3, 4], [5, 6]]
    tester2 = f6()(matrix2)
    assert next(tester2) == [1, 2]
    assert matrix2 == [[3, 4], [5, 6]]
    assert next(tester2) == [3, 5]
    assert matrix2 == [[4], [6]]
    assert next(tester2) == [4]
    assert matrix2 == [[6]]
    assert next(tester2) == [6]
    assert matrix2 == [[]]
    assert mat_gen_helper(tester2)


def mat_gen_helper(tester):
    """checks if there are no more iterations left. not an individual test"""
    try:
        next(tester)
    except StopIteration:
        return True
    else:
        return False
