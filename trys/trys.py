p = lambda x: print(x)


# # print(bool(())
#
# word='apple'
# x = set(word)
# y = ["w", "o","a", "r" , "d","D"]
# print()
# print(word, x)
# q = set(y)
# for i in q:
#     print(i)
#
# def gcd(x,y): #
#     while y > 0:
#         x,y = y, x % y
#     return x
#
# print(gcd(1488,724))


# itr_ob = [1,2,3,4,5]  ## map
# func = lambda x: x * x
# new_itr_ob =map(func, itr_ob)
# print(next(new_itr_ob))
# print(next(new_itr_ob))
# print(next(new_itr_ob))
# print(next(new_itr_ob))
# print(next(new_itr_ob))
# print(next(new_itr_ob))


# def factorial_list(n):   # !
#     return [list(range(1, i + 1)) for i in range(1, n + 1)]
# print(factorial_list(4))

# x='abcdef'
# y='' # empty string
# k=2
# print(x[0:k]+x[k+1:] , y+x[k])


# def f1(x, y=''): # y's default value is the empty string   # abc cba ....
#     if len(x) == 0:
#         print (y)
#     else:
#         for k in range(len(x)):
#             # f,g, h = x[0:k], x[k+1:] , y+x[k]
#             # print(f,g, h ,"t")
#             f1(x[0:k] + x[k+1:], y+x[k])


# from functools import reduce
#
# f = lambda x,y: [x, y]
#
# g =lambda x: -x if x % 2 == 0 else x
#
# print(reduce(f, map(g, range(6))))


# def f(n):
# #     if n< 10:
# #         return lambda x: x + n
# # print(f(4) (3))
# #
# #
# # class A:
# #     def __init__(self,im):
# #         self.im=im
# #
# #     def inv(self):
# #         self.im = -self.im
# #         return self
# #
# #     def add(self, a):
# #         self.im += a.im
# #         return self
# #
# #     def copy(self):
# #         return A(self.im)
# #
# #     def print(self):
# #         print(self.im)
# #         return self
# #
# # a = A(7)
# # a.print().add(a).print().copy().add(a.inv()).print()


# a = ['a', 'a', 'b', 'b', 'b', 'c', 'a', 'a']
#
# def fff(a):
#     # end_lst = []
#     # tmp = set(a)
#     # for v in tmp:
#     #     num = a.count(v)
#     #     end_lst.append((v, num))
#     # return end_lst
#     ans = []
#     run = 0
#     for i in range(len(a)):
#         if i == len(a) - 1 or a[i] != a[i + 1]:
#             ans.append((a[i], i - run + 1))
#             run = i
#     return ans

#
# def foo(n):
#     for i in range(n):
#         for k in range(1,i):
#             if k > n / k:
#                 return k
#
#
# foo(5)


# def h():
#     print("begin")
#     for i in range(2):
#         yield i
#         print('x_' + str(i))
#     print('end')
#
#
# z=h()
# x = next(z)
# next(z)
# print(x)


# def rec1(func, seq):
#     if seq:
#         return [func(seq[0])] + rec1(func, seq[1:])
#     else:
#         return []
#
# print(rec1(lambda x: int(x ** 0.5), [1, 100, 4, 64]))


# class Boss():
#     def __init__(self, name):
#         self.name = name
#
# a = Boss("Iosi")
# b = Boss("Ety")
# b.fast = False
# c = b
# c.old = True
# d = c
# c = a
# d.age = 42
#
# print(a.__dict__)
# print(b.__dict__)
# print(c.__dict__)
# print(d.__dict__)
#
# a = list(range(1,2))
# print(a)

# w = lambda x: x.upper()
# @w
# def say_hi():
#     return 'hey'
# print(say_hi)


# #
# class RANGE_D2:
#     def __init__(self, x ,y):
#         self.__x = x
#         self.__y = y
#
#
#     def __iter__(self):
#         for x in range(self.__x):
#             for y in range(self.__y):
#                 yield (x, y)

#
#     # def __str__(self):
#
# p = RANGE_D2(3, 2)
# for point in p: #iterate over all points in the Range2D
# print(point, end=" ")

#
# def subsets(lst):
#     if len(lst)==0:
#         yield []
#     else:
#         for tail in subsets(lst[1:]):
#             print(tail)
#             yield tail
#             print([lst[0]]+tail)
#             yield [lst[0]]+tail
#
#
#
# print(list(subsets([1,5,3])))


# from functools import reduce
#
# def count_appearances1(letter, word):
#     l = len(word)
#     fun = lambda letter, word: word.count(letter)
#     return reduce(fun, word,0)
#
# def count_appearances2(letter, word):
#
#     fun = lambda letter,y: if x in
#     return sum(map(fun, word))
#
# def count_appearances3(letter, word):
#
#     fun = lambda
#     return len(list(filter(fun, word)))
# #
#

# def f(n):
#     if n > 0:
#         return n * f(n - 1)
#     else:
#         return 1
#
#
# def exp_n_x(n, x):
#
#     if n < 0:
#         return
#     if n == 0:
#         return 1
#
#     else:
#         return ((x**n) / (f(n))) + exp_n_x(n - 1, x)
#
#
#
# print(exp_n_x(6,1))


# def help_up_and_right(n, k, lst, pat):
#     if (n, k) == (0, 0):
#         lst.append(pat)
#     if n != 0:
#         help_up_and_right(n - 1, k, lst, pat+ 'r')
#         # pat += "" + 'r'
#     if k != 0:
#         # pat += "" + 'u'
#         help_up_and_right(n, k - 1, lst, pat+ 'u')
#     return lst
#
#
# def up_and_right(n, k, lst):
#     x = help_up_and_right(n, k, lst, "")
#     return x
#
#
# print(up_and_right(2, 2, []))


# def permutations_dist(string, dist, tmp_step=0):
#     if tmp_step == len(string):
#         return 1
#     per_counter = 0
#     for i in range(tmp_step, len(string)):
#         lst_of_string = list(string)
#         lst_of_string[tmp_step], lst_of_string[i] = lst_of_string[i], lst_of_string[tmp_step]
#         if tmp_step < 1 or abs(
#                 ord(lst_of_string[tmp_step]) - ord(lst_of_string[tmp_step - 1])) <= dist:
#             per_counter += permutations_dist(lst_of_string, dist, tmp_step + 1)
#     return per_counter
#
#
# print(permutations_dist("abc", 1000))


# class CarDriver:
#     def __init__(self,s):
#         self.__skills = s
#
#     def get_skill(self):
#         return self.__skills
#
#
# class Car:
#     def __init__(self, speed):
#         self.__speed = speed
#         self.__driver = 1
#
#
#     def set_driver(self, driver_name):
#         self.__driver = driver_name
#
#
#     def get_driving_speed(self):
#         return self.__speed
#
# class RaceTrack:
#     def __init__(self, length):
#         self.__length = length
#         self.__cars = []
#
#     def race(self):
#         for car in Car.

# from functools import reduce
# def count_appearances2(letter, word):
#     word = list(word)
#     count = 0
#     r = range(len(word))
#     fun = lambda x: 1 if x == letter else 0
#     return sum(map(fun, word))
#
# def count_appearances3(letter, word):
#     word = list(word)
#     fun = lambda x:1 if x == letter else None
#     return len(list(filter(fun, word)))
#
# def count_appearances1(letter, word):
#     l = len(word)
#
#     fun = lambda x: 1 if x == letter else 0
#     return reduce(fun, word,0)
# #
# #
# print(count_appearances1('a', 'abcdaaca'))

#
#
# g = lambda x: x+7
# foo = lambda f: (lambda x:f(x+1)*2)
# print(g(3), (foo(g))(3), (foo(foo(g)))(3))
# print((foo(g))(3))


# def count_appearances1(letter, word):
#
#     fun = lambda count, y: count + (1 if y == letter else 0)
#     return reduce(fun, word, 0)
#
# #
# def count_appearances3(letter, word):
#     fun = lambda x:1 if x == letter else None
#     # fun = lambda x: x == letter
#     return len(list(filter(fun, word)))
# print(count_appearances3('l', 'wawlbcdelllw'))

# def my_range(n):
#     for i in range(n):
#         yield i
#
# x = iter(my_range(4))
# # x = list(my_range(4))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

#
# x = (i**2 -1 for i in range(77) if i != 0)
# print(type(x))
# print(next(x))


# def count(num):  # גנרטורים  שאלה טובה
#     print('num1 :', num)
#     if num <= 0:
#         return
#     for i in count(num - 1):
#         print('num2', num)
#         print('i :', i)
#         yield i
#     print('num3 :', num)
#     yield num
#
#
# for j in count(2):
#     print('out j:', j, end='\n')

# def g(x):
#     yield from range(x,0,-1)
#     yield from range(x)


# def t(x):
#     if x < 1:
#         return 0
#     return x + t(x-1)
# print(t(9))

# from itertools import cycle
# z = 'ofir the king '
# x = cycle(z)
#
# for i in range(len(z)):
#     print(next(x))

# a = [1,2,3,4,5]
# for i in range(a):

# class Range2D:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __iter__(self):
#         x,y =0,0
#         yield x, y
#         while (x,y )!= (self.__x,self.__y):
#             if next(self.__y) is not None:
#                 yield x,self.__y
#             if next(self.__x) is not None:
#                 yield self.__x, y
#                 x,y = self.__x, self.__y
#             yield x,y
#
# rect1 = Range2D(3,2)
# for point in rect1: #iterate over all points in the Range2D
#     print(point, end=" ")

# t = list('yes my good you'.split())
# d={'yes':'oui', 'good':'bien', 'night':'nuit', 'you':'toi'}
# f = { d[w] for w in d }
# ce = sum([1 for w in t if w in d])
# print(ce)
# print(t)


# def last_in(x):
#     first = x
#     yield None
#     while True:
#         after = x
#         yield first
#         first = x
#         yield after

#
# def t(x=2):
#     return 6 + x
#
#
# @t
# def g(t):
#     a =2
#     if True:
#         return a
#
# p(g(3))


# def f(a):
#     a[0] = 7
#     b[0] = 8
#
#
# a = [2]
# b = [3]
# f(b)
# p(b)
# p('a', a)
# f(a)
# p('a', a)

# def f():
#     p('f')
#
# f = lambda :p('s')
#
# p(f())

#
# class MyClass:
#     y = 0
#
#     def __init__(self, x):
#         self.x = MyClass.y
#         MyClass.y = x
#
#     def __str__(self):
#         return str(self.x)
#
# one = MyClass(1)
# two = MyClass(2)
# three = MyClass(3)
# print(MyClass.y, one, two, three)

# def zip_piz(*args):
#     while True:
#         args = [iter(arg) for arg in args]
#         values = [next(iterator, None) for iterator in args]
#         if False in (value is None for value in values):
#             yield (tuple(values))
#         else:
#             return
#
#
# for i in zip_piz(range(1), range(2), range(3), range(4)):
#     print(i)

# def noitcnuf(lst, n):
#     lst.append(n)
#     if n == 0:
#         raise ValueError()
#     else:
#         noitcnuf(lst, n - 1)
#     lst.pop()
#
# try:
#     lst = []
#     noitcnuf(lst, 4)
#     print("Hah!")
# except: pass
# finally: print(lst)


# def blurg(seq):
#     a = next(seq)
#     yield a
#     for b in seq:
#         mid = (a+b)//2
#         a = b
#         yield mid
#         yield b
#
#
# my_iter = iter([0, 8])
# x = blurg(my_iter)
# my_blurg = blurg(x)
# print(list(my_blurg))


# class ExamQuestion:
#     def __init__(self, id, difficulty=0, duration=0):
#         self.difficulty = difficulty
#         self.duration = duration
#         self.id = id
#
#
#     def __repr__(self):
#         return "q"+str(self.id)
#
#
# def my_key1(exam_question):
#     return exam_question.difficulty
#
#
# q1 = ExamQuestion(1,2,7)
# q2 = ExamQuestion(2,5,4)
# q3 = ExamQuestion(3,4,1)
# exam_questions = [q1,q2,q3]
#
# print(sorted(exam_questions, key=my_key1))


# def noitcnuf(lst, n):
#     lst.append(n)
#     if n == 0:
#         raise ValueError()
#     else:
#         noitcnuf(lst, n - 1)
#     lst.pop()
#
#
# try:
#     lst = []
#     noitcnuf(lst, 4)
#     print("Hah!")
# except:
#     pass
# finally:
#     print(lst)

# def d(iter1):
#     val1 = next(iter1)
#     for item in iter1:
#         yield item - val1
#         val1 = item
#
#
# def cs(iter1):
#     val1 = 0
#     yield val1
#     for item in iter1:
#         val1 += item
#         yield val1
#
#
# x = iter(range(5))
# y = d(cs(x))
# print(list(y))



# def f(lst):
# #     p(lst[1:])
# #     p(lst[:-1])
# #     # yt = lst[1:]+lst[:1]
# #     # p(yt)
# #     tmp = list(map(lambda x, y: x+y ,lst[1:],lst[:1]))
# #     # p(tmp)
# #     x,y,z =[lst[0]] , tmp , [lst[-1]]
# #     t =(x,y,z)
# #     # p(t)
# #     ans = [lst[0]] + tmp + [lst[-1]]
# #     return ans
# #
# #
# # p(f([1]))


# q = list(range(5))
# q1 = list(range(5,10))
# t = zip(q,q1)
# t= tuple(t)
# p(t)

# x = [None , 1]
# p(x)
#
#
#
# class Node:
#    def __init__(self, data):
#       self.data = data
#       self.next = None
#       self.prev = None
#
# class doubly_linked_list:
#
#    def __init__(self):
#       self.head = None
#
# # Adding data elements
#    def push(self, NewVal):
#       NewNode = Node(NewVal)
#       NewNode.next = self.head
#       if self.head is not None:
#          self.head.prev = NewNode
#       self.head = NewNode
#
# # Print the Doubly Linked list
#    def listprint(self, node):
#       while (node is not None):
#          print(node.data),
#          last = node
#          node = node.next
#
# dllist = doubly_linked_list()
# dllist.push(12)
# dllist.push(8)
# dllist.push(62)
# dllist.listprint(dllist.head)


# t = [x*2 for x in range(3)]
# p('t')
# p(t)
# y = [y for y in t]
# p('y')
# p(y)
#
# x = [x for x in [1,'1']]
#
# p('x')
# p(x)
#
# L = [x*y for x in [1,'1'] for y in t]
# print(L)
#
#


# h = lambda a, b: a if not b else h(a*a, b-1)
# f = lambda y, z: filter(y, z)
# g = lambda x: [x for x in range(int(x**0.5))]
#
# p(g(11))
# r = f(g, g(11))
# p(next(r))
# p(next(r))



# BRACKETS = {'{': '}', '(': ')', '[': ']'}

# def balanceBrack.ets(brackets):
#    stack = []
#    for b in brackets:
#       if b in BRACKETS:
#          stack.append(b)
#       elif stack and BRACKETS[stack[-1]]==b:
#          p(stack[-1])
#          p(BRACKETS[stack[-1]])
#          stack.pop()
#       else:
#          return False
#    return len(stack) == 0
#
#
# p(balanceBrackets('([]{})'))


# g = lambda f, x : f(f(x+1))
# f = lambda x: g((lambda y: y+10), x)
# p(f(7))
# p(g(f,7))
# print(f(7), g(f,7))

# d = {10:100, 20:200}
# e = {}
# for x in d: e[x+1], e[d[x]+2] = d[x]+3, d[x]+4
# print(e)
# p(d)

# w ={}
# for x in d: w[x+1], w


# class Node:
#     def __init__(self, data, next=None):
#         self.data, self.next = data, next
#
#
#     def __str__(self):
#         return str(self.data) +" " + str(self.next)
#
#
# def do_someting(head):
#     while head and head.next:
#         head.next.data, head.data = head.data, head.next.data
#         head = head.next
#
#
#
# head = Node(1,Node(2,Node(3,Node(4))))
# p(head)
# p(do_someting(head))
# p(do_someting(head))
# print(head)



# def set_p(s,n):
#     if n == 1:
#         return s
#     m, seter, lst,tmp, i = len(s), list(set(s)), [], [], 0
#     while len(lst) != m**n:
#         if len(tmp) == n:
#             lst.append(tmp)
#             tmp = []
#         tmp.append(seter[i])
#         i+=1
#         if i == len(seter):
#             i= 0
#
#     return lst
#
#
# # p(set_p([7,8],3))
#
#
# def set_power(s,n):
#
#     if n == 0: return [[]]
#     v = set_power(s, n-1)
#     ans = []
#     for t in v:
#         for x in s:
#             ans.insert(t + [x])
#     return ans
#
# p(set_power([7,8],3))
COUNT =0

# def foo(n):
#     global COUNT
#     for i in range(n):
#         COUNT +=1
#         for k in range(1,i):
#             COUNT += 1
#             if k>n/k:
#                 return COUNT
#
#
#
# p(foo(100))



# def h():
#     print("begin")
#     for i in range(2):
#         yield i
#         print('x_' + str(i))
#     print('end')
#
#
# z = h()
# next(z)
# next(z)


#
# def rec1(func, seq):
#     if seq:
#         return [func(seq[0])] + rec1(func, seq[1:])
#     else:
#         return []
#
#
# print(rec1(lambda x: int(x ** 0.5), [1, 100, 4, 64]))


# class A:
#     def __init__(self):
#         self.x = 1
#         A.y = 10
#
#     def f(self):
#         self.y += 10
#     def __repr__(self):
#         return str(A.y + self.x)
#
#
#
# d = A()
# p(d)
# d.f()
# p(d)

# def describe_str(st1):
#     return des_helper(st1, "",0)
#
# def des_helper(lst, result,index):
#     count=  same_char_helper(lst, index)
#     result += lst[index] + str(count)
#     index += count
#     if len(lst) == index:
#         return result
#     des_helper(lst, result, index)
#
# def  same_char_helper(s, k):
#     count ,lst = 0 , s[k:]
#     for chart in lst:
#         if chart == s[k]:
#             count+=1
#         else:
#             break
#     return count


def mat_gen():
    # tmp = []
    #
    # def g(mat):
    #     while mat:
    #         x = mat.pop(0)
    #         yield x
    #         for row in mat:
    #             tmp.append(row.pop(0))
    #         yield tmp
    #         tmp = []
    #
    #     return gen
    def transp(mat):
        return list(map(list, list(zip(*mat))))

    def gen(mat):
        while mat:
            yield mat[0]
            del mat[0]
            mat = transp(mat)

    return gen



# class A:
#     def __init__(self, x, d):
#         self.x = x
#         self.d = d
#         d[self.x] = len(self.d)
#
#
#     def copy(self):
#         return A(self.x, self.d)
#
#
#     def add(self, y):
#         self.x += y
#         self.d[self.x] = len(self.d)
#         return self
#
#
# first = A('', {}).add('A')
# second = first.copy().add('B')
# print(first.x, first.d)
# print(second.x, second.d)


# sub=lambda x,y: x-y
#
# def func(f, count=1):
#     if count > 1:
#         print(count)
#     count += 1
#     z=lambda x, y: f(x+1, y)
#     return z
#
# print(func(func(sub))(5, 3))


#
#
# d = [[1,9],'a', 2,'b', 3,'c', 4,'d']
# d= frozenset(d)
# for i in d:
#
#     p(i)
# tuple of vowels
# vowels = ('a', 'e', 'i', 'o', 'u','e')
#
# fSet =set(vowels)
# print('The frozen set is:', fSet)
# print('The empty frozen set is:', frozenset())
#
# # frozensets are immutable
# fSet.add('v')
# print('The frozen set is:', fSet)

#
# L1=[1,2,3,7]
# L2=[11,22,33,44]
# L3=[12,23,43,54]
# L4 = [1,1,1,1]
# lst=[]
# for i in zip(L1,L2,L3,L4 ):
#     lst.append(i[0]*i[1]-i[2]+i[3])
#
# p(lst)


# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))
#
#     # Driver code
#
#
# myFun(first='Geeks', mid='for', last='Geeks')


def generate(n):
    if n>1:
        for i in generate(n-1):
            # p(i)
            # p(n)
            # p("")
            yield i*2
    yield 1

lst = list(generate(6))
print(lst)