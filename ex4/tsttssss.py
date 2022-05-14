
from hangman import *
#
#     for i in W:
#         while len(pattern) == len(W[i]):  #### כמות איברים
#             for j in W[i]:
#                 while pattern[j] != '_' and j <= len(pattern[j]):
#                     for W[i][j] == pattern[j]:
#                         if j == len(pattern):
#                             tmp.append(W[i])
#
#     for k in tmp:
#         for z in wrong_guess_lst:
#             if z in tmp:
#                 break
#             else:
#                 matches.append(k)
#     return matches
# print(filter_words_list())


words = ['aardvark', 'aardwolf', 'aaron', 'aback', 'abacus', 'abaft',
         'abalone', 'abandon', 'abandoned', 'abandonment', 'abandons',
         'abase', 'abased', 'abasement', 'abash', 'abashed', 'abate',
         'abated', 'abatement', 'abates', 'abattoir', 'abattoirs', 'abbe',
         'abbess', 'abaged', 'abcdef']
pattern = '_b____'



# abates

wrong_guess_lst = ['g']



def filter_words_list(words, pattern,wrong_guess_lst):
    matches = []
    words = ['abcdef','aardvark', 'aardwolf', 'aaron', 'aback', 'abacus', 'abaft',
             'abalone', 'abandon', 'abandoned', 'abandonment', 'abandons',
             'abase', 'abased', 'abasement', 'abash', 'abashed', 'abate',
             'abated', 'abatement', 'abates', 'abattoir', 'abattoirs', 'abbe',
             'abbess', 'abaged', 'abcdef']
    pattern = '_b____'
    wrong_guess_lst = ['g']

    for single_word in  words:
        if len(single_word) == len(pattern):
            if compere_pattern_word((single_word, pattern)):
                if check_letter(single_word, wrong_guess_lst):
                    matches.append(single_word)

    return matches


print(filter_words_list(words, pattern,wrong_guess_lst))

#
        # if pattern[i] != '_':
        #     for let in the_word:
        #         if pattern[i] != let:
        #             return False
        # if len(the_word) == i+1:
        #     return True
        #
        #         ## חדש
        # for j in range(len(pattern)):
        #     if pattern[j] != '_':
        #         if pattern[j] != the_word[i]:
        #             return False
        #
        #         if j == len(pattern)-1:
        #             return True
        #

        # for let in the_word:
        #     if let in pattern: