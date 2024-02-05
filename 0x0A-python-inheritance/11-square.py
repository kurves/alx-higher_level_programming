#!/usr/bin/python3

"""base geometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Public instance method to calculate the area."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """public instance method to validate an integer value."""
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
        """public instance method to calculate the area of the rectangle."""
        return self.__width * self.__height


class Square(Rectangle):
    """square class inherits from Rectangle"""

    def __init__(self, size):
        """Initializes a Square instance with the given size."""
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def __str__(self):
        """Returns the square description as a string."""
        return f"[Square] {self.__size}/{self.__size}"
