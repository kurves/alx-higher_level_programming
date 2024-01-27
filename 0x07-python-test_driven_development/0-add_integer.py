#!/usr/bin/python3

"""
function thats integres
return ann integer
Raises typeError
"""


def add_integer(a, b=98):
    """
    adds two integers a and b and returns an int
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
