#################################################################
# FILE : wave_editor.py
# EXERCISE : intro2cs2 ex6 2020
# DESCRIPTION: program that edit wav files and allows composing
# with a file that contains multiple characters and the playback
# time of each character
#################################################################
import math
import wave_helper as wh

DEF_SAMPLE_RATE = 2000
MAX_VAL = 32767
MIN_VAL = -32768

CHANGE_FILE = '1'
COMPOSE_SOUND = '2'
EXIT = '3'

REVERSE_WAV = '1'
NEGATIVE_WAV = '2'
SPEED_UP = '3'
SLOW_DOWN = '4'
TURN_UP = '5'
TURN_DOWN = '6'
FADE_FILTER = '7'
QUIET = '8'

OPTIONS_LST = [REVERSE_WAV, NEGATIVE_WAV, SPEED_UP, SLOW_DOWN, TURN_UP,
               TURN_DOWN, FADE_FILTER, QUIET]
CHANG_OPTIONS_STR = ('Press The Num Of The Option You Want To Change\n1 For '
                     'Reverse\n2 For Negative Sound '
                     '\n3 For Speed Up Sound\n4 For Slow Down Sound\n5 For '
                     'Turning Up The Volume '
                     '\n6 For Turning Down The Volume\n7 For Fade Filte\n8 '
                     'To Save And Exit')

CHANGE_SOUND = 'Wave File Have been Updated'
WRONG_CHOICE = 'Wrong Choice!\n'
WRONG_INPUT_FILE = 'Wrong Input File!'
WRONG_WAVE_FILE = 'Wrong wave File!'
RENAME_REQUEST_MSG = "please insert the name of the file that you want to " \
                     "compose: "
CHANGE_FILE_NAME_MSG = "Write The Name Of The File You Want To Change:"
SAVE_FILE = 'Choose File Name For Saving:'
MANE_MENU_MSG = "Press 1 For Changing Wave File \nPress 2 For Composing " \
                "Sound \nPress 3 For Exit "

PIE = math.pi

A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'
F = 'F'
G = 'G'
Q = 'Q'
FREQ_A = 440
FREQ_B = 494
FREQ_C = 523
FREQ_D = 587
FREQ_E = 659
FREQ_F = 698
FREQ_G = 784
FREQ_Q = 0

CHORD_LST = [A, B, C, D, E, F, G, Q]
CHANGE_VOL = 1.2


def reverse_wav(lst):
    """
    Get list of lists and return reversed list
    """
    reverse_lst = lst[:]
    reverse_lst.reverse()
    return reverse_lst


def negative_wav(lst):
    """
    Get list of lists and return negative list
    """
    negative_lst = lst[:]
    for i in range(len(negative_lst)):
        for j in range(len(negative_lst[i])):
            if negative_lst[i][j] == MIN_VAL:
                negative_lst[i][j] = MAX_VAL
            else:
                negative_lst[i][j] = -int(negative_lst[i][j])
    return negative_lst


def speed_up_wav(lst):
    """
        Get list of lists and return speed up list
    """
    speed_up_lst = []
    for i in range(0, len(lst), 2):
        speed_up_lst.append(lst[i])
    return speed_up_lst


def slow_down_wav(lst):
    """
        Get list of lists and return slow down list
    """
    slow_down_lst = []
    temp_lst = []
    for i in range(len(lst)):
        slow_down_lst.append(lst[i])
        if i == len(lst) - 1:
            break
        for j in range(len(lst[i])):
            sum_avg = int((lst[i][j] + lst[i + 1][j]) / 2)
            temp_lst.append(sum_avg)
        slow_down_lst.append(temp_lst)
        temp_lst = []
    return slow_down_lst


def turn_up_wav(lst):
    """
        Get list of lists and return list that turn up the volume
    """
    turn_up_lst = []
    temp_lst = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            the_sum = int(CHANGE_VOL * lst[i][j])
            if the_sum > MAX_VAL:
                the_sum = MAX_VAL
            elif the_sum < MIN_VAL:
                the_sum = MIN_VAL
            temp_lst.append(the_sum)
        turn_up_lst.append(temp_lst)
        temp_lst = []
    return turn_up_lst


def turn_down_wav(lst):
    """
           Get list of lists and return list that turn down the volume
    """
    turn_down_lst = []
    temp_lst = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            the_sum = int(lst[i][j] / CHANGE_VOL)
            if the_sum < MIN_VAL:
                the_sum = MIN_VAL
            temp_lst.append(the_sum)
        turn_down_lst.append(temp_lst)
        temp_lst = []
    return turn_down_lst


def fade_filter(lst):
    """
    the function Get list of lists and return list with the fade effect
    """
    fade_filter_lst = []
    temp_lst = []
    if len(lst) == 1:
        return lst
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if i == 0:
                the_sum = int((lst[i][j] + lst[i + 1][j]) / 2)
            elif i == len(lst) - 1:
                the_sum = int((lst[i - 1][j] + lst[i][j]) / 2)
            else:
                the_sum = int((lst[i - 1][j] + lst[i][j] + lst[i + 1][j]) / 3)
            temp_lst.append(the_sum)
        fade_filter_lst.append(temp_lst)
        temp_lst = []
    return fade_filter_lst


def change_wav_options_menu(lst):
    """
    function that is responsible for file changes based on user input
    """
    sample_rate = lst[0]
    sound_lst = lst[1]
    print(CHANG_OPTIONS_STR)
    option_input = input()
    while option_input != QUIET:
        if option_input not in OPTIONS_LST:
            print(WRONG_CHOICE)
            print(CHANG_OPTIONS_STR)
            option_input = input()
        else:
            sound_lst = find_the_right_change_path(sound_lst,
                                                   option_input)
            print(CHANGE_SOUND)
            print(CHANG_OPTIONS_STR)
            option_input = input()
    return save_menu(sample_rate, sound_lst)


def find_the_right_change_path(sound_lst, num):################################
    """
    A function responsible for making changes to the file according to the
    input from the function "change_wav_options_menu(lst)"
    """
    output_sound = []
    if num == REVERSE_WAV:
        output_sound = reverse_wav(sound_lst)
    if num == NEGATIVE_WAV:
        output_sound = negative_wav(sound_lst)
    if num == SPEED_UP:
        output_sound = speed_up_wav(sound_lst)
    if num == SLOW_DOWN:
        output_sound = slow_down_wav(sound_lst)
    if num == TURN_UP:
        output_sound = turn_up_wav(sound_lst)
    if num == TURN_DOWN:
        output_sound = turn_down_wav(sound_lst)
    if num == FADE_FILTER:
        output_sound = fade_filter(sound_lst)
    if num == QUIET:
        return output_sound
    return output_sound


def composing_per_chord(sample_for_cycle, num_per_six_ten):
    """
    function that accepts the cities according to sample for cycle,
    num per six ten  by which it returns the list
    """
    new_wave = []
    for i in range(int((DEF_SAMPLE_RATE * int(num_per_six_ten)) / 16)):
        if sample_for_cycle == 0:
            tmp_sample = 0
        else:
            tmp_sample = int(
                MAX_VAL * math.sin(2 * PIE * (i / sample_for_cycle)))
        new_wave.append([tmp_sample, tmp_sample])
    return new_wave


def find_sample_for_cycle(chord_frequency):
    """
    function that finds it and returns the value sample for cycle by formula
    """
    if chord_frequency == FREQ_Q:
        return chord_frequency
    sample_for_cycle = DEF_SAMPLE_RATE / chord_frequency
    return sample_for_cycle


def open_composing_file(file_name):
    """
    function that opens the composer file and returns a list of the values
  ​​in the file
    """
    with open(file_name, 'r') as chord_string:
        the_chord = chord_string.read()
        the_chord_lst = the_chord.split()
    return the_chord_lst


def build_compose_list(tup_lst):
    """
     function that get List of tupples, check it and return list of the
     sound data
    """
    compose_lst = []
    if tup_lst == WRONG_INPUT_FILE:
        return tup_lst
    for sum_per_cyc, num_per_sixt in tup_lst:
        sample = composing_per_chord(sum_per_cyc, num_per_sixt)
        for i in range(len(sample)):
            compose_lst.append(sample[i])
    return compose_lst


def check_composing_file(the_chord_lst):
    """
    Checking the composer file
    :param the_chord_lst:  list
    :return:If the file have a problem returns an error message
    Otherwise returns list of tuples
    """
    tup_lst = []
    for i in range(0, len(the_chord_lst), 2):
        if the_chord_lst[i] not in CHORD_LST:
            return WRONG_INPUT_FILE
    for i in range(1, len(the_chord_lst), 2):
        if int(the_chord_lst[i]) < 0:
            return WRONG_INPUT_FILE
    for i in range(0, len(the_chord_lst), 2):
        if i == len(the_chord_lst) - 1:
            break
        tup = find_sample_for_cycle(find_freq_by_chord(the_chord_lst[i])), \
              the_chord_lst[i + 1]
        tup_lst.append(tup)
    return tup_lst


def find_freq_by_chord(chord_str):
    """
    A function that correlates the chord with its frequency
    :param chord_str:
    :return:
    """
    if chord_str not in CHORD_LST:
        return False
    if chord_str == A:
        chord_str = FREQ_A
    if chord_str == B:
        chord_str = FREQ_B
    if chord_str == C:
        chord_str = FREQ_C
    if chord_str == D:
        chord_str = FREQ_D
    if chord_str == E:
        chord_str = FREQ_E
    if chord_str == F:
        chord_str = FREQ_F
    if chord_str == G:
        chord_str = FREQ_G
    if chord_str == Q:
        chord_str = FREQ_Q
    return chord_str


def change_wav_menu():
    """
    The changes menu for wave file
    :return:the change in the wave file
    """
    print(CHANGE_FILE_NAME_MSG)
    fle_name = input()
    output_lst = wh.load_wave(fle_name)
    while output_lst == -1:
        print(WRONG_WAVE_FILE, '\n')
        print(CHANGE_FILE_NAME_MSG)
        fle_name = input()
        output_lst = wh.load_wave(fle_name)
    return change_wav_options_menu(output_lst)


def comp_menu():
    """
    Composing menu
    :return:If the file have a problem returns an error message
    Otherwise returns the frequency list
    """
    the_comp_file_name = input(RENAME_REQUEST_MSG)

    comp_file = open_composing_file(the_comp_file_name)
    sound_lst = []
    check = check_composing_file(comp_file)
    if check != WRONG_INPUT_FILE:
        sound_lst.append(DEF_SAMPLE_RATE)
        sound_lst.append(build_compose_list(check))
        return sound_lst
    else:
        return check


def save_menu(sample_rate, sound_lst):
    """
    A function that is responsible for saving the wave file
    """
    print(SAVE_FILE)
    file_save = input()
    wh.save_wave(sample_rate, sound_lst, file_save)


def print_and_choice():
    """
    print the main menu massage and ask for input from the user
    :return: the input from the user
    """
    print(MANE_MENU_MSG)
    choice = input()
    return choice


def main_menu():
    """ The main function that regulates the operations in the program"""
    choice = print_and_choice()
    while choice != '3':
        if choice != str(CHANGE_FILE) and choice != str(COMPOSE_SOUND) and \
                choice != str(EXIT):
            print(WRONG_CHOICE)
            choice = print_and_choice()
            continue
        if choice == CHANGE_FILE:
            change_wav_menu()
        if choice == COMPOSE_SOUND:
            output = comp_menu()
            if output != WRONG_INPUT_FILE:
                change_wav_options_menu(output)
        if choice == EXIT:
            break
        choice = print_and_choice()


if __name__ == '__main__':
    main_menu()
