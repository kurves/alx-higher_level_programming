#!/usr/bin/python3
"""base class base geometry"""


class BaseGeometry:
    """BaseGeometry class with area and integer_validator methods."""

    def area(self):
        """Public instance method to calculate the area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Public instance method to validate an integer value."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance with given width and height."""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Public instance method to calculate the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the rectangle description as a string."""
        return f"[Rectangle] {self.__width}/{self.__height}"
