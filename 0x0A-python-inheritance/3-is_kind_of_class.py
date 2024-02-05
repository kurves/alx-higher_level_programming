#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """
    Function to check if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.

    Parameters:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of, or if the object is an instance
        of a class that inherited from, the specified class; otherwise False.
    """
    return isinstance(obj, a_class)
