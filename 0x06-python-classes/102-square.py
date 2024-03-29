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
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size():
        """
        Set the size.

        Args:
            value (int): The size of each side.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
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
    def __gt__(self, other):
        """Define the greater than comparator."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented
    def __ge__(self, other):
        """Define the greater than or equal comparator."""
        if isinstance(other, Square):
            return self.area() >= other.area(
        return NotImplemented

    def __lt__(self, other):
        """Define the less than comparator."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """Define the less than or equal comparator."""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented
     def __eq__(self, other):
        """Define the equality comparator."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Define the not equal comparator."""
        return not self.__eq__(other)
