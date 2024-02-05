#!/usr/bin/python3

def add_attribute(obj, attr, value):
    """
    Adds a new attribute
    Raises a TypeError
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
