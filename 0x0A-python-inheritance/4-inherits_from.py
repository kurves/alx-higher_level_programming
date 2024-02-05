#!/usr/bin/python3
"""function to compate classess"""


def inherits_from(obj, a_class):
    """(directly or indirectly) from the specified class"""
    if isinstance(type(obj), a_class):
        return True
    for parent in obj.__class__.__bases__:
        if inherits_from(parent, a_class):
            return True

    return False
