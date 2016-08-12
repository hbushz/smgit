#! /usr/local/bin/python3

class Student(object):
    def __init__(self,name):
        self.name = name

shuomo=Student('Shuomo Zhang')
shuomo.score=90

if hasattr(shuomo,'score'):
    print(shuomo.score)

def set_age(self,age):
    self.age=age

Student.set_age=set_age
shuomo.set_age(34)
print(shuomo.age)

zhou=Student('Zhou huan')
zhou.set_age(18)
print(zhou.age)
