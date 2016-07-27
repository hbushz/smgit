#! /usr/local/bin/python3

def by_name(student):
    return student[0].lower()

L=[('Bob',10),('Alice', 100),('Bart', 60),('Lisa', 75)]

Ls=sorted(L,key=by_name)

print(Ls)
