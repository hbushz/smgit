#! /usr/bin/python3

# Day 1
# age = 2
# if age >= 18:
#     print('Hello world, I am adult')
# else:
#     print('Hello world, I am young')

# Day 2
# a = "张素恒"
# b = a
# a = 123
# print('my name is %s.' % b)

# Day 3 list and tuple
# myfamily = ['zhang', 'zhou', 'yuan', 'dian']
# print('The length of myfamily list is %d.' % len(myfamily))
# for name in myfamily:
#     print('They are %s' % name)

# myfamily = ('zhang', 'zhou', 'yuan', 'dian')
# print('The length of myfamily list is %d.' % len(myfamily))
# for name in myfamily:
#     print('They are %s' % name)

# Day 4 dictionary
# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 0:
#         # continue
#         break
#     print(n)

# myfamily = {'zhang': 35, 'zhou': 35, 'yuan': 6, 'dian': 1}
# for nam in myfamily:
#     print('%s is %d years old.' % (nam, myfamily[nam]))

# Day 5 function
# import math

# def quadratic(a, b, c):
#     if b*b >= 4*a*c:
#         x1 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
#         x2 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
#     else:
#         raise TypeError('no real root')
#     return x1, x2

# x1, x2 = quadratic(1, 5, 3)
# print(x1, x2)

# def calc(*num):
#     sum = 1
#     for n in num:
#         sum = sum*n
#     return sum

# num = (1, 2, 3, 4)
# print(calc(*num))

# def fact(n):
#     if n == 1:
#         return 1
#     return n*fact(n-1)

# print(fact(10))

# def move(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         move(n-1, a, c, b)
#         move(1, a, b, c)
#         move(n-1, b, a, c)

# move(3, "A", "B", "C")

# def findMinandMax(L):
#     if L == []:
#         return (None, None)
#     min = L[0]
#     max = L[0]
#     for t in L:
#         if t > max:
#             max = t
#         elif t < min:
#             min = t
#     return min, max

# print(findMinandMax([0, 1, 10, 0, 2]))
# print(findMinandMax([]))

# import os

# d = [d for d in os.listdir('.')]
# for myhome in d:
#     print(myhome)

# Fibonacci list generator
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a+b
#         n = n + 1
#     return "done"

# for n in fib(5):
#     print(n)

# Yanghui Triangle generator
# def yht(N):
#     n = 1
#     yhl = [1]
#     while n <= N:
#         yield yhl
#         yhl = list(map(lambda m, n: m+n, [0]+yhl, yhl+[0]))
#         n = n+1
#     return 'Done'

# for yhlist in yht(6):
#     print(yhlist)

# Day 2018-06-22 class
# class Student(object):
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Student.count = Student.count + 1

# shuomo = Student('zhangSuheng')
# shuomo = Student('zhangSuheng')
# print(Student.count)

# class Student(object):

#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return 'Student object (%s)' % self.name

#     @property
#     def birth(self):
#         return self._birth

#     @birth.setter
#     def birth(self, year):
#         if not(isinstance(year, int)):
#             raise ValueError('score must be an integer.')
#         elif (year <= 1900 or year > 2018):
#             raise ValueError('you must make a mistake!')
#         else:
#             self._birth = year

#     @property
#     def score(self):
#         return self._score

#     @score.setter
#     def score(self, value):
#         if not(isinstance(value, int)):
#             raise ValueError('score must be an integer.')
#         elif (value < 0 or value > 100):
#             raise ValueError('score should be 0~100.')
#         else:
#             self._score = value

#     @property
#     def age(self):
#         return 2018-self._birth

# shuomo = Student('shz')
# shuomo.birth = 1990
# shuomo.score = 100
# print(shuomo)
# print(shuomo.name, shuomo.birth, shuomo.age, shuomo.score)

# Day 2018-06-27 class
# from urllib import request, parse
# from datetime import datetime

# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/5.0'
# }
# dit = {
#     'name': 'China'
# }
# data = bytes(parse.urlencode(dit), encoding='utf8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# res = request.urlopen(req)
# print(res.read())
# print(datetime.now())

# Day 2018-08-15 function
# from functools import reduce
# from operator import add

# ans1 = reduce(add, range(100))
# ans2 = sum(range(100))
# print(ans1, ans2)
# print(callable(add))

# 可调用对象( 调用运算符() )
# import random

# class BingoCage(object):
#     def __init__(self, items):
#         self._items = list(items)
#         random.shuffle(self._items)

#     def pick(self):
#         try:
#             return self._items.pop()
#         except IndexError:
#             raise LookupError('pick from empty BingoCage')

#     def __call__(self):         # 可调用对象需要的函数
#         return self.pick()

# bingo = BingoCage(range(3))
# print(bingo())
# print(bingo())
# print(bingo())

# Day 2018-08-17 function
# 函数注解
# def sum(x: int, y: 'int > 0') -> int:
#     pass

# for key, v in sum.__annotations__.items():
#     print(key)
#     print(v)

# 支持函数式编程的包
# from functools import reduce
# from operator import mul

# def fact(n):
#     return reduce(mul, range(1, n+1))

# num = fact(20)
# print(num)

# Day 2018-08-18 function
# from operator import itemgetter

# cdate = [('Tokyo', 'JP', (1, 2)),
#          ('Shanghai', 'SH', (3, 4)),
#          ('Anguo', 'AG', (6, 4)),
#          ('Mexico City', 'MX', (4, 5))
#          ]
# # for city in sorted(cdate, key=itemgetter(0)):
# #     print(city)

# index = itemgetter(1, 0)
# for cname in cdate:
#     print(index(cname))

# from collections import namedtuple

# Card = namedtuple('Card', ['rank', 'suit'])
# mycard = Card('7', 'clubs')
# print(mycard)

# class Porker(object):
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     suits = 'spade diamonds clubs hearts'.split()

#     def __init__(self):
#         self._cards = [
#             Card(rank, suit) for suit in self.suits for rank in self.ranks
#         ]

#     def __len__(self):
#         return len(self._cards)

#     def __getitem__(self, position):
#         return self._cards[position]

# deck = Porker()
# for n in range(len(deck)):
#     print(deck[n])

# Day 2018-08-18 closure
# def creatcounter(b=0):
#     t = b

#     def counter():
#         nonlocal t
#         t = t + 1
#         return t

#     return counter

# count = creatcounter(10)
# count()
# print(count())
# print(count())
# print(count())

# Day 2018-08-22 装饰器
import time


def clock(func):
    def clocked(*args):
        t0 = time.time()
        result = func(*args)
        elapsed = time.time() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def sum(a, b):
    return a + b


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(1.234)')
    snooze(1.234)
    sum(1, 2)
    print('*' * 40, 'Calling factorial(10)')
    print('10!=', factorial(10))
