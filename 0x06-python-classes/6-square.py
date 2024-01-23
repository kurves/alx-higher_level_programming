#!/usr/bin/python3

"""DEFINE CLASS"""


class Square:
    """class defining a class"""
    def __init__(self, size=0, position=(0, 0)):
        """
        initializes a new instance of class
        Args:
            size(int): optoonal
        Raises:
            TypeError: if not int
            ValueError: if less than 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size.

        Args:
            value (int): The size of each side.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Get theposition of the square."""
        return self.__position

    @size.setter
    def position(self, value):
        """
        Set the position

        Args:
            value (tuple): The position (x,y)
        Raises:
            TypeError: If value is not a tuple
            ValueError: if tuple contains invalid values.
        """
        if not isinstance(value, tuple) or \
                len(value) != 2 or not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        calculates and return area
        Returns: int
        """
        return self.__size ** 2

    def my_print(self):
        """prints the area"""
        if self.__size == 0:
            print()
            return
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
