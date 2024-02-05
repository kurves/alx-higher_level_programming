#!/usr/bin/python3

def add_attribute(obj, attr, value):
    """
    Adds a new attribute

    Raises a TypeError

    Parameters:
        obj: The object to which the attribute is to be added.
        attr (str): The name of the attribute to add.
        value: The value of the attribute to add.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
