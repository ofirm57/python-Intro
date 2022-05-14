from collections import Counter
word= 'bob'
x= "bobobob"
y= x.count('bob',-1)

print(y)

x=[]
for i in x:
    x[i] = x[::-1]
print(x)


# for let_x in x:
#     n = 0
#     result = []
#     word_count = len(word)
#     for let_word in word:
#         if let_x == let_word:
#             n += 1
#         else:
#             n = 0
#         if word_count == n:
#             result.append(word)
#             n -= 1
#
# print(result)
#
# row = 'bobobob'
# word_check = 'bob'
# word_len = len(word_check)
# matches_number = 0
# for index in range(len(row)):
#     if row[i:i + word_len] == word_check:
#         matches_number += 1
# return matches_number


# def count_substring(string,sub_string):
#     l=len(sub_string)
#     count=0
#     for i in range(len(string)-len(sub_string)+1):
#         if(string[i:i+len(sub_string)] == sub_string ):
#             count+=1
#     return count


# print(count_substring(x,word))
# def the_finder(word_file_lst, the_matrix):
#     results = []
# #     for word in word_file_lst:
#         length = len(word)
#         for i in the_matrix:
#             n = 0
#             for j in i:
#                 if j == word[n]:
#                     n += 1
#                 else:
#                     n = 0
#                 if n == length:
#                     results.append(word)
#                     n = 1
#     return results
