#! /usr/local/bin/python3

import re

pattern=re.compile(r'hello')
match=pattern.match('hello shuomo')
if match:
    print(match.group())
