#!/usr/bin/python3
class Square:
    """class defining a class"""
    def __init__(self, size=0):
        """
        initializes a new instance of class
        Args:
            size(int): optoonal
        Raises:
            TypeError: if not int
            ValueError: if less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """
        calculates and return area
        Returns: int
        """
        return self.__size ** 2 

