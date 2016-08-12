#! /usr/local/bin/python3

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("You call %s():" % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print("2016-07-28")

now()
print(now.__name__)
