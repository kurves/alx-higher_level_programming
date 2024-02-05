#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    (directly or indirectly) from the specified class.

    Parameters:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the objecly or indirectly) from the specified class; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
     for parent in obj.__class__.__bases__:
        if inherits_from(parent, a_class):
            return True

    return False
