# taken from kifi interview:
# implement the square root function using a continuous binary search and x^2.
delta = 0.0000000000001

def sqrt(x):
    def recurse(lower, upper):
        midpoint = (upper + lower) / 2
        squared = midpoint * midpoint
        if abs(squared - x) < delta:
            return midpoint
        elif x > squared:
            return recurse(midpoint, upper)
        else:
            return recurse(lower, midpoint)
    if x == 1:
        return 1
    elif x > 1:
        return recurse(1, 1000)
    else:
        return recurse(0, 1)

def sqrt_iter(x):
    if x == 1:
        return 1

    if x > 1:
        lower = 1
        upper = 1000
    else:
        lower = 0
        upper = 1

    # from stack overflow http://stackoverflow.com/questions/743164/emulate-a-do-while-loop-in-python
    # do-while equivalent in python:
    while True:
        midpoint = (upper + lower) / 2
        squared = midpoint * midpoint
        if abs(squared - x) < delta:
            return midpoint
        elif x > squared:
            lower = midpoint
        else:
            upper = midpoint

import math

assert sqrt(1) == 1
assert abs(sqrt(2) - math.sqrt(2)) < delta
assert abs(sqrt(4) - math.sqrt(4)) < delta
assert abs(sqrt(0.5) - math.sqrt(0.5)) < delta