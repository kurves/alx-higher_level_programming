#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Function to check if the object is exactly an instance of the specified class.

    Parameters:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True  otherwise False.
    """
    return type(obj) == a_class
