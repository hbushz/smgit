#! /usr/local/bin/python3

class Student(object):

    def __init__(self, name, score):
        self.name=name
        self.score=score

    def __len__(self):
        return self.score

    def __get_grade(self):
        if self.score >=90:
            return "A"
        elif self.score >=60:
            return "B"
        else:
            return "C"

    def print_score(self):
        print('%s: %d %s' % (self.name,self.score,self.__get_grade()))

alice=Student("Alice",100)
alice.print_score()
alice._Student__get_grade()
print(len(alice))
