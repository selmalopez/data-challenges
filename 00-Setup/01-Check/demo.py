"""Dummy challenge for Kitt Demo"""
from math import pi


def circle_area(radius):
    try:
        return pi * (radius * radius)

    except ValueError:
        print('invalid code')
        # handle ValueError exception
    pass
    # handle ValueError exception
# YOUR CODE HERE
