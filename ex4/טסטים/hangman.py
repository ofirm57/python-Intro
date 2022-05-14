from hangman_helper import *

REPLAY_MSG = ''
GAME_DATA = 'your score is {} and number of game is: {}'
WRONG_INPUT_MSG = 'wrong input!!! try again'
GUESS_ALREADY_MSG = 'you guess that letter already ,try again '
CORETTE_GUESS = 'You guessed the {} right'
MISTAKE_GUESS = 'You guessed it wrong '
YOU_WIN_MSG = ', you win!!!'
LOOSE_MSG = 'you loose!!! ,the word was "{}" '  # game_word
PLAY_AGAIN = 'you played {} games. if you want to play again press y, else n'
ALPHABET = list("abcdefghijklmnopqrstuvwxyz")


def update_word_pattern(word, pattern, letter):
    """ :param word: string
    :param pattern: string
    :param letter: string
    :return: pattern with the letter that we enter this function in string
    with length of the word"""
    lst = [list(word), list(pattern), letter]
    counter = -1
    for j in lst[0]:
        counter += 1
        if letter == j:
            lst[1][counter] = letter
    new_pattern = ''.join(lst[1])
    return new_pattern  ##### ??


def check_letter(word, wrong_guess_lst):
    """Checks if the word does'nt contain the letters in the incorrect guess
    list.
    :param word: string
    :param wrong_guess_lst: list of letters the user guessed and was incorrect
    :return:False if the letter is contained in the word, True if not """
    for i in range(len(word)):
        if word[i] in wrong_guess_lst:
            return False
    return True


def compere_pattern_word(single_word, pattern):
    """Checks if the word contains exactly the same letters in the same
    positions of the letters visible in the pattern and these letters are not
     found Elsewhere in the filtered word.
        :param single_word: string
        :param pattern:string
        :return:True if the word meets the conditions else:False """
    if not single_word.islower():
        return False
    for i in range(len(single_word)):
        if pattern[i] != '_':
            if single_word[i] != pattern[i]:
                return False
            if pattern.count(pattern[i]) != single_word.count(pattern[i]):
                return False
        if i == len(pattern) - 1:
            return True


def hint_length_check(matches):
    """ :param matches:List of appropriate words for hint
    :return:A list contains fewer organs, which is determined by the value
    HINT_LENGTH and the condition of this program"""
    matches_new = []
    if len(matches) > HINT_LENGTH:
        n = len(matches)
        for i in range(HINT_LENGTH):
            matches_new.append(matches[int((i * n) / HINT_LENGTH)])
    return matches_new


def filter_words_list(words_list, pattern, wrong_guess_lst):
    """:param words_list: list of words      :param  pattern: current pattern
    :param wrong_guess_lst:
    :return:List of words that meet the length conditions and the functions:
    "compere_pattern_word","check_letter" and "hint_length_check"  """

    matches = []
    for single_word in words_list:
        if len(single_word) == len(pattern):
            if compere_pattern_word(single_word, pattern):
                if check_letter(single_word, wrong_guess_lst):
                    matches.append(single_word)
    if len(matches) > HINT_LENGTH:
        matches = hint_length_check(matches)
    return matches


def run_single_game(words_list, score=POINTS_INITIAL):
    """function that runs a single game
    :param words_list: list of word     ,    :param score: User score.
    :return:new score  """
    game_word = get_random_word(words_list)
    wrong_guess_lst = []
    pattern = '_' * len(game_word)
    msg = ''
    while score >= 0:
        display_state(pattern, wrong_guess_lst, score, msg)
        if pattern == game_word or score <= 0:
            break
        guess = get_input()

        (msg, pattern, score) = letter_from_user(game_word, guess, msg, pattern
                                                 , score, wrong_guess_lst)
        # USE THE FUNCTION "letter_from_user"
        score = ask_for_hint(guess, pattern, score, words_list,
                             wrong_guess_lst)
        # USE THE FUNCTION : "ask_for_hint"
        (msg, pattern, score) = word_from_user(game_word, guess, msg, pattern,
                                               score)
        # USE THE FUNCTION : "word_from_user"
    return score


def ask_for_hint(guess, pattern, score, words_list, wrong_guess_lst):
    """:param guess:user input ,       :param pattern: the current pattern
       :param score: the current score    :param words_list:
       :param wrong_guess_lst:
    show suggestions of words that match the current pattern and :return:
    the new score """
    if guess[0] == HINT_LENGTH:
        score -= 1
        tmp_msg = filter_words_list(words_list, pattern, wrong_guess_lst)
        show_suggestions(tmp_msg)
    return score


def word_from_user(game_word, guess, msg, pattern, score):
    """A function that works when the user guesses a whole word and updates
     the variables that depend on the guess.
    :param game_word:The word a user has to guess
       :param guess: guess:user input ,    :param msg:Message to the user
       :param score:                       :param pattern: the current pattern
       :return:the new:msg, score and pattern"""
    n = 0  ######
    if guess[0] == WORD:
        if len(guess[1]) != len(game_word):
            msg = WRONG_INPUT_MSG.format('isnt')
        if guess[1] != game_word:
            score -= 1
            msg = MISTAKE_GUESS
        if guess[1] == game_word:  ####
            n -= 1
            n = pattern.count('_')
            score += int(n * (n + 1) / 2)
            msg = CORETTE_GUESS.format('word') + YOU_WIN_MSG
            pattern = game_word
        if score <= 0:  ######
            msg = MISTAKE_GUESS + LOOSE_MSG.format(game_word)
    return msg, pattern, score


def letter_from_user(game_word, guess, msg, pattern, score, wrong_guess_lst):
    """A function that works when the user guesses a letter and updates
     the variables that depend on the guess.
    :param game_word:The word a user has to guess
    :param guess: guess:user input ,    :param msg:Message to the user
    :param score:                       :param pattern: the current pattern
    :param wrong_guess_lst: List of incorrectly guessed letters
    :return:the new:msg, score and pattern"""

    while guess[0] == LETTER:
        if guess[1] not in ALPHABET:
            msg = WRONG_INPUT_MSG
            break
        if (guess[1] in wrong_guess_lst) or (guess[1] in pattern):
            msg = GUESS_ALREADY_MSG
            break
        else:
            score -= 1
            if guess[1] not in game_word:
                wrong_guess_lst.append(guess[1])
                if score <= 0:
                    msg = MISTAKE_GUESS + LOOSE_MSG.format(game_word)
                    break
                msg = MISTAKE_GUESS
                break
            if guess[1] in game_word:
                pattern = update_word_pattern(game_word, pattern, guess[1])
                n = pattern.count(guess[1])
                score += int(n * (n + 1) / 2)
                msg = CORETTE_GUESS.format('letter')
                if pattern == game_word:
                    msg += YOU_WIN_MSG
                break
    return msg, pattern, score


def main():
    """Function that performs the actions:
    1) Loads the words using the "load_words" function
    2) Single game stimulant
    3) Allows further games to run (by scoring) """

    global score  ####
    words_list = load_words(file='words.txt')
    game_num = 0
    while True:
        if game_num == 0:
            game_num += 1
            score = run_single_game(words_list, POINTS_INITIAL)
        if score >= 1:
            while play_again(GAME_DATA.format(score, game_num) + REPLAY_MSG):
                score = run_single_game(words_list, score)
                game_num += 1
        if score < 1:
            if play_again(GAME_DATA.format(score, game_num - 1)):
                game_num = 1###
                continue
            else:
                break
        else:

            break


if __name__ == "__main__":
    main()
