#!/usr/bin/python3
"""function to add atrributre"""


def add_attribute(obj, attr, value):
    """Adds a new attribute"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
