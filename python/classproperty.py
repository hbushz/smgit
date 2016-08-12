#! /usr/local/bin/python3
class Student(object):
    def __init__(self,name):
        self.__name=name

    @property
    def score(self):
        return self._myscore

    @score.setter
    def score(self, value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value<0 or value>100:
            raise ValueError('score must between 0~100')
        self._myscore=value

shuomo=Student("Zhang Suheng")
shuomo.score=60
print(shuomo.score)
