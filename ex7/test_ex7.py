################################################
# File: test_ex7.py
# Writer: Dor Roter 
# Login: dor.roter
# Exercise: ------
# More:
#       Consulted: -----      
#       Internet: 
#       Notes: 
################################################

import ex7
import hanoi
import itertools
import math

STRICT_HANOI = True


def is_prime(n):
    return n > 1 and all(n % i for i in itertools.islice(itertools.count(2),
                                                         int(math.sqrt(n) - 1)))


def check_parentheses(string):
    count = 0
    for i in string:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0


def check_print_n(n):
    s = ""
    for i in range(1, n + 1):
        s += str(i) + "\n"
    return s


def check_sum(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def test_print_to_n(capsys):
    exp = ""
    for n in range(1, 57):
        ex7.print_to_n(n)
        exp += check_print_n(n)

    captured = capsys.readouterr()
    assert captured.out == exp


def test_digit_sum():
    for n in range(0, 100000):
        assert check_sum(n) == ex7.digit_sum(n), "Mismatch in: " + str(n)


def test_is_prime():
    for i in range(10000):
        assert ex7.is_prime(i) == is_prime(i), "Mismatch in: " + str(i)


def test_print_sequences(capsys):
    tests = [
        ([], 7),
        (["a"], 7),
        (["a", "b"], 7),
        (["a", "b"], 2),
        (["a", "b", "c"], 2),
        (["a", "b", "c", "d", "e", "f"], 3),
        (["a", "b", "c", "7", "&"], 2),
        (["a", "b", "c", "7", "&"], 5),
        (["a", "b", "c", "7", "&"], 0)
    ]

    for test in tests:
        ex7.print_sequences(*test)
        expected = ["".join(c) for c in
                    (itertools.product(test[0], repeat=test[1]))]
        expected = [] if expected == [''] else expected
        output = capsys.readouterr().out.split()
        output.sort(), expected.sort()
        assert expected == output, "failed in case: " + str(test)


def test_print_no_repetition(capsys):
    tests = [
        ([], 0),
        (["a"], 1),
        (["a", "b", "c"], 1),
        (["a", "b", "c"], 0),
        (["a", "b", "c"], 2),
        (["3", "2", "1", "4", "5", "6", "7"], 4),
        (["a", "b", "c"], 2),
        (["a", "b", "c", "5", ";"], 4),
    ]

    for test in tests:
        ex7.print_no_repetition_sequences(*test)
        expected = ["".join(c) for c in itertools.permutations(*test)]
        expected = [] if expected == [''] else expected
        captured_seq = capsys.readouterr().out.split()
        captured_seq.sort(), expected.sort()
        assert captured_seq == expected, "failed in case: " + str(test)


def parentheses_opt_num(n):
    return (math.factorial(2 * n) / (math.factorial(n) * math.factorial(n))) / (
                n + 1)


def test_parentheses():
    for i in range(0, 10):
        lst = ex7.parentheses(i)

        assert len(lst) == parentheses_opt_num(i), "incorrect number of options"
        for string in lst:
            assert check_parentheses(string), "option '" + string + "' is invalid"


def test_flood_fill():
    O = '.'
    I = O
    X = '*'
    tests = [
        (
            [
                [X, X, X, X, X],
                [X, I, X, O, X],
                [X, O, X, O, X],
                [X, X, X, X, X]
            ],
            (1, 1),
            [
                [X, X, X, X, X],
                [X, X, X, O, X],
                [X, X, X, O, X],
                [X, X, X, X, X]
            ]
        ),
        (
            [
                [X, X, X, X, X],
                [X, I, X, O, X],
                [X, O, O, O, X],
                [X, X, X, X, X]
            ],
            (1, 1),
            [
                [X, X, X, X, X],
                [X, X, X, X, X],
                [X, X, X, X, X],
                [X, X, X, X, X]
            ]
        ),
        (
            [
                [X, X, X, X, X],
                [X, O, X, O, X],
                [X, O, O, O, X],
                [X, X, X, X, X]
            ],
            (0, 0),
            [
                [X, X, X, X, X],
                [X, O, X, O, X],
                [X, O, O, O, X],
                [X, X, X, X, X]
            ]
        ),
        (
            [
                [X, X, X, X, X],
                [X, O, X, I, X],
                [X, O, X, O, X],
                [X, X, X, X, X]
            ],
            (2, 3),
            [
                [X, X, X, X, X],
                [X, O, X, X, X],
                [X, O, X, X, X],
                [X, X, X, X, X]
            ]
        ),
        (
            [
                [X, X, X],
                [X, I, X],
                [X, X, X]
            ],
            (1, 1),
            [
                [X, X, X],
                [X, X, X],
                [X, X, X]
            ]
        ),
        (
            [
                [X, X, X, X, X, X, X, X, X],
                [X, X, X, X, O, X, X, X, X],
                [X, X, O, X, O, X, O, X, X],
                [X, X, X, X, O, X, X, X, X],
                [X, O, O, O, I, O, O, X, X],
                [X, X, X, X, O, X, X, X, X],
                [X, X, X, X, O, X, X, X, X],
                [X, X, O, X, O, X, O, X, X],
                [X, X, X, X, O, X, X, X, X],
                [X, X, X, X, X, X, X, X, X]
            ],
            (4, 4),
            [
                [X, X, X, X, X, X, X, X, X],
                [X, X, X, X, X, X, X, X, X],
                [X, X, O, X, X, X, O, X, X],
                [X, X, X, X, X, X, X, X, X],
                [X, X, X, X, X, X, X, X, X],
                [X, X, X, X, X, X, X, X, X],
                [X, X, X, X, X, X, X, X, X],
                [X, X, O, X, X, X, O, X, X],
                [X, X, X, X, X, X, X, X, X],
                [X, X, X, X, X, X, X, X, X]
            ]
        ),
        (
            [
                [X, X, X, X, X, X, X, X, X],
                [X, X, O, X, O, X, O, X, X],
                [X, O, O, O, I, O, O, X, X],
                [X, X, X, X, O, X, X, X, X],
                [X, X, X, X, O, X, X, X, X],
                [X, X, X, X, X, X, X, X, X]
            ],
            (2, 4),
            [
                [X, X, X, X, X, X, X, X, X],
                [X, X, X, X, X, X, X, X, X],
                [X, X, X, X, X, X, X, X, X],
                [X, X, X, X, X, X, X, X, X],
                [X, X, X, X, X, X, X, X, X],
                [X, X, X, X, X, X, X, X, X]
            ]
        ),
        (
            [
                [X, X, X, X, X, X, X, X, X],
                [X, O, O, O, O, X, O, O, X],
                [X, O, O, O, I, O, O, X, X],
                [X, O, O, X, O, X, X, X, X],
                [X, O, O, O, O, X, X, O, X],
                [X, X, X, X, X, X, X, X, X]
            ],
            (2, 4),
            [
                [X, X, X, X, X, X, X, X, X],
                [X, X, X, X, X, X, X, X, X],
                [X, X, X, X, X, X, X, X, X],
                [X, X, X, X, X, X, X, X, X],
                [X, X, X, X, X, X, X, O, X],
                [X, X, X, X, X, X, X, X, X]
            ]
        )
    ]

    IMAGE = 0
    START = 1
    EXPECTED = 2
    for test in tests:
        ex7.flood_fill(test[IMAGE], test[START])
        assert test[IMAGE] == test[EXPECTED], "failed in case: " + str(test)


def test_hanoi():
    for i in range(-5, 20):
        mock_hanoi = hanoi.MockHanoi()
        ex7.play_hanoi(mock_hanoi, i, 'A', 'B', 'C')
        assert mock_hanoi.validate_moves(i), "a move preformed was illegal"
        if STRICT_HANOI:
            assert mock_hanoi.is_minimum(i), "isn't the minimum moves number"

