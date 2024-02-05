#!/usr/bin/python3

"""Define a class base geometry ande ares"""


class BaseGeometry:
    """class defining a class"""
    def area(self):
        """
        Public instance method to calculate the area.

        Raises:
            Exception: Always raises an exception with the message 'area() is not implemented'.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):

        """
        initializes a new instance of class
        Args:
            size(int): optoonal
        Raises:
            TypeError: if not int
            ValueError: if less than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
