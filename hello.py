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
