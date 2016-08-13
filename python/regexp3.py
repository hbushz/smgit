#! /usr/bin/python

import re

m=re.match(r'(\w+) (\w+)(?P<id>.*)','hello world!!')

# some property for match object
print("m.string: %s" % m.string)
print("m.re: %s" % m.re)
print("m.pos: %s" % m.pos)
print("m.endpos: %s" % m.endpos)
print("m.lastgroup: %s" % m.lastgroup)


# some method for match object
print("m.group(1,2,3): %s\t%s\t%s" % m.group(1,2,3))
print("m.groupdict(): %s" % m.groupdict())
print("m.span(2):begin index:%s end index plus one:%s" % m.span(2))
print(r"m.expand(r'\g<id> \2 \1'): %s" % m.expand(r'\g<id> \2 \1'))
