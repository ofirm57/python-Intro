import os
import sys
import hashlib

import wave_editor
from wave_editor import *
import wave_helper

# !!!!!!!!!! CHANGE HERE !!!!!!!!!!
REVERSE_FUNC = wave_editor.reverse_wav
SLOW_FUNC = wave_editor.slow_down_wav
FAST_FUNC = wave_editor.speed_up_wav
VOLUME_UP_FUNC = wave_editor.turn_up_wav
VOLUME_DOWN_FUNC = wave_editor.turn_down_wav
BLUR_FUNC = wave_editor. fade_filter
# OFF_FUNC = wave_editor.audio_off

COMPOSE_BY_FILE_FUNC = wave_editor.composing_per_chord
# CALCULATE_SAMPLE_FUNC = wave_editor.get_compose_input

# !!!!!!!!!! CHANGE HERE END !!!!!!!!!!


def test_reverse():
    lst = [[10, 20], [30, 40], [50, 60], [70, 80]]
    REVERSE_FUNC(lst)
    assert lst == \
           [[70, 80], [50, 60], [30, 40], [10, 20]]
    lst = [[10, 20]]
    REVERSE_FUNC(lst)
    assert lst == \
           [[10, 20]]
    lst = [[-100, 100], [-2, -2], [0, 0]]
    REVERSE_FUNC(lst)
    assert lst == \
           [[0, 0], [-2, -2], [-100, 100]]
    lst = [[1, 1], [0, 0]]
    REVERSE_FUNC(lst)
    assert lst == \
           [[0, 0], [1, 1]]
    lst = [[111111, 30000], [30000, 111111]]
    REVERSE_FUNC(lst)
    assert lst == \
           [[30000, 111111], [111111, 30000]]
    lst = [[1, 0]]
    REVERSE_FUNC(lst)
    assert lst == \
           [[1, 0]]
    lst = []
    REVERSE_FUNC(lst)
    assert lst == \
           []


def test_slow():
    assert SLOW_FUNC([[10, 20], [30, 40], [50, 60], [70, 80]]) == \
           [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70],
            [70, 80]]
    assert SLOW_FUNC([[0, 0], [0, 0], [0, 0], [0, 0]]) == \
           [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    assert SLOW_FUNC([[-32768, -32768], [32767, 32767]]) == \
           [[-32768, -32768], [0, 0], [32767, 32767]]
    assert SLOW_FUNC([[-32768, -32768], [-32768, -32768]]) == \
           [[-32768, -32768], [-32768, -32768], [-32768, -32768]]
    assert SLOW_FUNC([[0, 5], [5, 0]]) == \
           [[0, 5], [2, 2], [5, 0]]
    assert SLOW_FUNC([[0, 5], [5, 0]]) == \
           [[0, 5], [2, 2], [5, 0]]
    assert SLOW_FUNC([[0, 5]]) == \
           [[0, 5]]
    assert SLOW_FUNC([[]]) == \
           [[]]


def test_fast():
    assert FAST_FUNC([[10, 20], [30, 40], [50, 60], [70, 80]]) == \
           [[10, 20], [50, 60]]
    assert FAST_FUNC([[1, 1], [0, 0]]) == \
           [[1, 1]]
    assert FAST_FUNC([[0, 0]]) == \
           [[0, 0]]
    assert FAST_FUNC([]) == []


def test_volume_up():
    assert VOLUME_UP_FUNC([[10, 20], [30, 40], [50, 60], [70, 80]]) == \
           [[12, 24], [36, 48], [60, 72], [84, 96]]
    assert VOLUME_UP_FUNC([[1, 1], [0, 0]]) == \
           [[1, 1], [0, 0]]
    assert VOLUME_UP_FUNC([[32766, -32766], [0, 1], [5, -5]]) == \
           [[32767, -32768], [0, 1], [6, -6]]
    assert VOLUME_UP_FUNC([[32766, 32766], [-32760, -32750]]) == \
           [[32767, 32767], [-32768, -32768]]
    assert VOLUME_UP_FUNC([[1, 1]]) == \
           [[1, 1]]
    assert VOLUME_UP_FUNC([[]]) == \
           [[]]


def test_volume_down():
    assert VOLUME_DOWN_FUNC(
        [[10, 20], [30, 40], [50, 60], [70, 80]]) == \
           [[8, 16], [25, 33], [41, 50], [58, 66]]
    assert VOLUME_DOWN_FUNC([[1, 1], [0, 0]]) == \
           [[0, 0], [0, 0]]
    assert VOLUME_DOWN_FUNC([[32767, -32768], [5, -5]]) == \
           [[27305, -27306], [4, -4]]
    assert VOLUME_DOWN_FUNC([[32767, 32767], [-32768, -32768]]) == \
           [[27305, 27305], [-27306, -27306]]
    assert VOLUME_DOWN_FUNC([[1, 1]]) == \
           [[0, 0]]
    assert VOLUME_DOWN_FUNC([[]]) == \
           [[]]


def test_blur():
    assert BLUR_FUNC([[10, 20], [30, 40], [50, 60], [70, 80]]) == \
           [[20, 30], [30, 40], [50, 60], [60, 70]]
    assert BLUR_FUNC( [[0, 0], [0, 0], [0, 0]]) == \
           [[0, 0], [0, 0], [0, 0]]
    assert BLUR_FUNC([[1, 1], [1, 1], [1, 1]]) == \
           [[1, 1], [1, 1], [1, 1]]
    assert BLUR_FUNC([[1, 1], [0, 0]]) == \
           [[0, 0], [0, 0]]
    assert BLUR_FUNC([[32766, -32766], [0, 1], [5, -5]]) == \
           [[16383, -16382], [10923, -10923], [2, -2]]
    assert BLUR_FUNC([[1, 1]]) == \
           [[1, 1]]
    assert BLUR_FUNC([[]]) == \
           [[]]


def test_off():
    assert OFF_FUNC(
        [[10, 20], [30, 40]]) == \
           [[-10, -20], [-30, -40]]
    assert OFF_FUNC(
        [[], []]) == \
           [[], []]
    assert OFF_FUNC(
        [[-10, 20], [-30, 40]]) == \
           [[10, -20], [30, -40]]
    assert OFF_FUNC(
        [[0, 0], [30, 40]]) == \
           [[0, 0], [-30, -40]]
    assert OFF_FUNC(
        [[0, 0]]) == \
           [[0, 0]]
    assert OFF_FUNC(
        [[-32768, 32767]]) == \
           [[32767, -32767]]


def test():
    print("test starts here:")
    test_reverse()
    test_slow()
    test_fast()
    test_volume_down()
    test_volume_up()
    test_blur()
    test_off()
    print("all tests passed")


test()
