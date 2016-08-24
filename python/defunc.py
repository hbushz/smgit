#! /usr/local/bin/python3
import math
def quadratic(a,b,c):
    if a==0:
        raise ValueError("a can't be 0")
    if b*b-4*a*c>=0:
        return (-b-math.sqrt(b*b-4*a*c))/(2*a),(-b+math.sqrt(b*b-4*a*c))/(2*a)
    else:
        print("There is no real root for this function.")
        return

root=quadratic(1,4,-21)
print(root)

