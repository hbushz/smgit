#! /usr/local/bin/python3

with open('/Users/SHZ/smgit/python/hello.py','r') as f:
    for line in f.readlines():
        print(line.strip())
