import nonogram
import ex8_helper

#######
# nonograms taken from https://webpbn.com

def test_count_row_variations():
    LONG_TEST = [((3, [1, 1]), 1), ((3, [1]), 3), ((3, [1, 2]), 0), ((7, [2, 1,
                                                                          1]),
                                                                     4), ((10,
                                                                           [2,
                                                                            1,
                                                                            1,
                                                                            2]),
                                                                          5),
                 ((11, [2, 1, 1,
                        3]), 5), ((12, [2, 2, 1, 3]), 5),
                 ((14, [3, 3, 1, 3]), 5), ((14, [2, 4, 2, 2]), 5),
                 ((16, [4, 4, 1, 3]), 5), ((16, [2, 2, 1, 1, 5]), 6),
                 ((21, [5, 2, 4, 6]), 5), ((18, [5, 5, 1, 3]), 5),
                 ((19, [2, 4, 2, 7]), 5), ((22, [1, 1, 4, 7, 4]), 6),
                 ((24, [5, 1, 8, 6]), 5), ((28, [6, 1, 7, 1, 8]), 6),
                 ((23, [5, 8, 1, 2, 2]), 6), ((23, [5, 3, 2, 9]), 5),
                 ((27, [9, 10, 5]), 4), ((29, [4, 10, 4, 7]), 5),
                 ((28, [6, 10, 9]), 4), ((32, [7, 5, 6, 10]), 5),
                 ((29, [9, 4, 3, 9]), 5), ((30, [11, 7, 4, 1, 2]), 6),
                 ((30, [8, 5, 11, 2]), 5), ((40, [13, 1, 12, 10]), 5),
                 ((40, [5, 3, 4, 10, 13]), 6), ((45, [8, 7, 2, 11, 12]), 6),
                 ((41, [4, 7, 14, 12]), 5), ((45, [12, 11, 7, 11]), 5),
                 ((46, [16, 15, 12]), 4), ((37, [10, 14, 10]), 4),
                 ((42, [11, 5, 8, 2, 11]), 6), ((41, [11, 11, 16]), 4),
                 ((44, [14, 10, 17]), 4), ((44, [4, 2, 3, 7, 1, 7, 13]), 8),
                 ((51, [3, 14, 13, 17]), 5), ((45, [12, 7, 12, 3, 6]), 6),
                 ((44, [13, 9, 19]), 4), ((51, [16, 4, 4, 11, 11]), 6),
                 ((45, [6, 20, 16]), 4), ((47, [16, 12, 16]), 4),
                 ((55, [20, 17, 3, 11]), 5), ((60, [9, 1, 13, 2, 13, 16]), 7),
                 ((53, [4, 4, 13, 2, 12, 12]), 7),
                 ((52, [1, 1, 17, 14, 14]), 6), ((67, [24, 14, 1, 24]), 5),
                 ((56, [20, 22, 11]), 4), ((60, [15, 19, 8, 14]), 5),
                 ((62, [20, 9, 4, 2, 22]), 6),
                 ((76, [13, 10, 6, 1, 18, 1, 2, 17]), 9),
                 ((62, [22, 5, 7, 4, 19]), 6), ((72, [24, 15, 13, 16]), 5),
                 ((63, [8, 17, 8, 26]), 5), ((61, [10, 19, 11, 17]), 5),
                 ((76, [22, 25, 8, 17]), 5), ((61, [11, 29, 18]), 4),
                 ((73, [2, 24, 2, 5, 23, 11]), 7)]
    SHORT_TEST = [((3, [1, 1]), 1), ((3, [1]), 3), ((3, [1, 2]), 0),
                  ((7, [2, 1, 1]), 4), ((10, [2, 1, 1, 2]), 5),
                  ((11, [2, 1, 1, 3]), 5),
                  ((12, [2, 2, 1, 3]), 5), ((14, [3, 3, 1, 3]), 5),
                  ((14, [2, 4, 2, 2]), 5)]

    for (length, blocks), count in LONG_TEST:
        actual = nonogram.count_row_variations(length,blocks)
        assert actual == count, \
            print(f"INPUT: length:{length}\nblocks:{blocks}\n EXPECTED:" \
            f"{count}\nACTUAL:{actual}")

def test_get_row_variations():
    TEST_DATA = [(([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, -1],[2]),[[0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0]]),(([0,-1,0,1,1,1,1,1,1,1,1,1,1,1,1,
-1],[13]),[[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1]])]


    for (row, blocks), expected in TEST_DATA:
        actual = nonogram.get_row_variations(row, blocks)
        assert actual == expected, \
            print(f"INPUT: row:{row}\nblocks:{blocks}\n EXPECTED:" \
                  f"{expected}\nACTUAL:{actual}")

def test_easy_solve():
    TEST_DATA = [([[[4, 1], [2, 1], [2, 3], [2, 3], [1, 1, 3], [4, 3], [3], [4, 3], [1, 1, 3], [2, 3], [2, 3], [2, 3], [4, 3], [3], [1, 3], [2, 3], [1, 3], [1, 3], [1, 3], [3, 5], [5], [7], [2, 2]], [[1, 2, 2, 2, 1, 1], [1, 1, 1, 1, 3, 6], [4, 1, 1, 2, 1, 1], [2, 3, 3, 1, 2], [4], [20], [22], [20], [4], [2]]], [[1, 1, 1, 1, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 1, 0, 0, 0], [0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1, 1, 1, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0], [1, 1, 1, 1, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 0, 0], [1, 1, 1, 1, 0, 1, 1, 1, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1, 1, 1, 0, 0], [0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 1, 1, 1, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 0, 0], [0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1, 0, 0], [0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 1, 1, 0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1]]), ([[[3], [5, 3], [6, 5], [7, 6], [6, 7], [7, 6], [7, 4], [7, 3], [5, 4], [3, 4], [3, 4], [1, 3], [1, 3], [2], [1]], [[5], [8], [9], [11], [12], [9], [1, 4, 3], [2, 4], [1, 4], [3, 4], [9], [9], [8], [6], [4]]], [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]), ([[[6], [10], [13], [15], [5, 7], [5, 5, 6], [4, 8, 6], [4, 10, 5], [4, 4, 4, 6, 1, 1], [3, 3, 2, 3, 5, 1, 1], [3, 3, 5, 2, 5, 1, 1], [3, 3, 5, 3, 4, 3], [3, 3, 2, 2, 3, 4, 5], [4, 3, 3, 3, 4, 5], [4, 6, 3, 5, 5], [5, 4, 4, 6, 4], [5, 4, 7, 4], [11, 9, 4], [9, 9, 5], [5, 8, 6], [7, 8], [6, 10], [25], [26], [26]], [[7, 1], [11, 2], [13, 2], [6, 5, 3], [5, 4, 5, 3], [5, 7, 4, 4], [4, 9, 4, 4], [4, 4, 3, 3, 4], [4, 4, 3, 2, 3, 4], [4, 3, 4, 2, 3, 4], [4, 3, 3, 3, 3, 4], [4, 4, 5, 3, 1, 3], [5, 3, 4, 4, 1, 3], [4, 4, 4, 2, 3], [5, 10, 3, 3], [5, 7, 4, 3], [7, 3, 5, 3], [8, 7, 3], [16, 4], [15, 4], [14, 4], [11, 5], [4, 5], [1, 6], [1, 7], [2, 13], [1, 13], [14], [10], [3]]], [[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0], [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0], [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0], [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]), ([[[7], [3, 1, 3], [2, 1, 2], [3, 1, 3], [2, 2, 1, 2, 2], [1, 7, 1], [1, 1, 1], [15], [1, 1, 1], [1, 7, 1], [2, 2, 1, 2, 2], [3, 1, 3], [2, 1, 2], [3, 1, 3], [7]], [[7], [3, 1, 3], [3, 1, 3], [1, 2, 1, 2, 1], [2, 2, 1, 2, 2], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [15], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [2, 2, 1, 2, 2], [1, 2, 1, 2, 1], [3, 1, 3], [3, 1, 3], [7]]], [[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0], [1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1], [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0], [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]), ([[[10, 10], [8, 7], [6, 5], [5, 1, 4], [4, 3, 3], [3, 6, 2], [2, 5, 1], [2, 5, 1], [1, 6], [1, 6], [8], [1, 10], [4, 8, 2], [16, 2], [16, 2], [18], [16], [16], [16], [18], [13, 3], [6, 4, 2], [4, 12], [1, 3, 5, 3, 1, 1], [1, 3, 1, 3, 4, 1, 1], [2, 2, 1, 2, 7, 2], [3, 2, 4, 1, 6, 3], [4, 3, 4, 1, 6, 4], [5, 5, 14], [7, 3, 2, 2, 11]], [[10, 7], [8, 5], [6, 3, 4], [5, 3, 3], [4, 3, 2], [3, 4, 1], [2, 3, 1], [2, 4], [1, 1, 5, 1], [1, 1, 8, 1, 2, 1], [26], [23, 2], [20, 3], [18, 6], [16, 1, 4], [14, 5], [11, 4, 2], [2, 8, 3, 4], [1, 10, 1, 1], [2, 8, 6], [1, 18], [1, 17], [1, 6, 8], [2, 3, 1, 5], [2, 2, 8], [3, 1, 1, 2], [4, 2, 1, 3], [5, 3, 4], [6, 2, 5], [8, 7]]], [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), ([[[2, 2, 3], [1, 1, 3], [4, 2, 9], [26], [2, 10, 4], [2, 1, 1, 3], [1, 3, 2, 1, 2], [1, 1, 10, 1, 1], [2, 4, 9], [2, 4, 9], [3, 4, 10], [1, 4, 4, 10], [24], [1, 11, 2, 12], [11, 5, 10], [10, 1, 1, 1, 9], [10, 7, 7], [9, 1, 1, 1, 6, 1], [9, 1, 1, 1, 1, 3, 2], [8, 2, 2, 1, 2], [6, 1, 1, 2], [5, 2, 2], [3, 2, 1, 6], [3, 9, 2], [21]], [[1, 6], [1, 1, 3, 6], [3, 2, 7], [3, 9, 1], [1, 11, 1], [1, 11, 1], [1, 11, 1], [1, 12, 1], [2, 10, 1], [1, 2, 9, 1], [5, 9, 2], [5, 2, 5, 2], [2, 11, 1, 3], [2, 8, 1, 1, 2, 1], [2, 6, 4, 1, 1], [12, 1, 1, 1], [2, 2, 5, 1, 1], [2, 6, 5, 2], [2, 7, 2], [2, 9, 3], [2, 12, 2], [1, 2, 13, 2], [4, 11, 2], [4, 11, 3], [3, 10, 2], [2, 11, 3], [3, 7, 3], [3, 4, 2, 1], [4, 2, 2, 2], [4, 1, 2, 1]]], [[0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]]), ([[[1, 6, 7, 6, 1], [1, 5, 1, 1, 1, 1, 5, 1], [1, 4, 1, 1, 1, 4, 1], [1, 3, 9, 3, 1], [1, 3, 11, 3, 1], [1, 2, 2, 2, 2, 1], [1, 2, 1, 11, 1, 2, 1], [1, 2, 15, 2, 1], [3, 2], [1, 10], [1, 11], [1, 10], [1, 10], [1, 10], [1, 2, 7], [1, 3, 6], [1, 4, 6], [1, 4, 6], [2, 3, 8], [2, 4, 8], [3, 4, 9], [2, 5, 8], [3, 4, 9], [3, 3, 9], [4, 5, 10], [3, 7, 10], [2, 8, 8], [1], [3], [1]], [[8, 2], [4], [8, 5], [8, 5], [5, 5], [3, 15, 1], [2, 1, 2, 1], [1, 5, 1, 2], [4, 2, 1, 3, 2], [1, 2, 2, 2, 7, 3], [2, 2, 2, 18], [1, 2, 2, 18, 1], [1, 3, 2, 5, 3, 5, 2], [1, 2, 2, 6, 3, 2, 2], [2, 2, 2, 14], [1, 2, 2, 17], [4, 2, 18], [1, 4, 18], [2, 1, 2, 17], [3, 3, 17], [5, 9], [8, 7], [8, 5], [4], [8, 2]]], [[1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1], [1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), ([[[15], [18], [20], [23], [17, 5], [18, 5], [19, 5], [18, 7], [29], [30], [30], [30], [30], [31], [5, 9, 10], [4, 7, 9], [3, 6, 8], [3, 3, 5, 3, 8], [2, 3, 1, 5, 2, 1, 8], [2, 3, 1, 5, 3, 2, 8], [2, 5, 4, 6, 8], [3, 4, 6, 8], [3, 2, 2, 2, 4, 9], [4, 1, 4, 9], [5, 12], [3, 9], [2, 9], [2, 9], [3, 2, 10], [4, 3, 4, 5], [6, 4, 1, 4, 3], [12, 3, 5, 2], [5, 2, 5, 2], [2, 3, 3, 6, 2], [3, 3, 4, 9], [4, 8, 8], [4, 6, 7], [4, 4, 7], [4, 6], [3, 6]], [[4], [5], [18, 6], [33], [13, 15], [13, 3, 2, 5], [13, 5, 1, 5], [13, 7, 5], [13, 1, 3, 2, 3], [15, 4, 1, 3], [17, 1, 1, 3], [20, 1, 1, 3], [21, 1, 3], [21, 1, 3], [21, 2, 2], [21, 1, 1, 2], [16, 1, 1, 1], [15, 1, 2], [14, 3, 1, 2], [14, 6, 1, 2], [14, 7, 2, 2], [7, 6, 1, 4, 1, 1], [4, 6, 7, 2], [4, 8, 3, 2], [4, 9, 1], [32], [32], [33], [34], [24, 9], [22, 7], [21, 6], [18, 6], [18], [12]]], [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1], [0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]])]

    for (const,expected) in TEST_DATA:
        actual = nonogram.solve_easy_nonogram(const)
        assert actual == expected, \
            print(f"INPUT: constraints:{const}\nEXPECTED:" \
                  f"{expected}\nACTUAL:{actual}")
