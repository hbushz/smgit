#! /usr/bin/python

import re
p=re.compile(r'(\w+) (\w+)')
s='I say, hello Ping'
print(p.match(s).group())

print(p.sub(r'\2 \1',s))

def func(m):
    return m.group(1).upper()+' '+m.group(2).lower()

print(p.sub(func,s))
