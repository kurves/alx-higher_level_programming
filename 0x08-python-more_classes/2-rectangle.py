#!/usr/bin/python3

"""DEFINE CLASS"""


class Rectangle:
    """class defining a width attribute"""
    def __init__(self, width, height):
        """
        initializes a new instance of class
        Args:
            width(int)
            height(int)
        Raises:
            TypeError: if not int
            ValueError: if less than 0
        """
        self.width = width
        self.height= height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the size.

        Args:
            value (int): The size of each side.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get theposition of the square."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height

        Args:
            height:int
        Raises:
            TypeError: If value is not int
            ValueError: if height contains invalid values.
        """
        if not isinstance(value, int):
            raise TypeError("height  must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        calculates and return area
        Returns: int
        """
        return self.height * self.width

    def perimeter(self):
        """
        calculates and return perimeter
        Returns: int
        """
        return 2 * (self.height + self.width) if self.width != 0 and self.height != 0 else 0
