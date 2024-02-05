#!/usr/bin/python3

"""base geometry class"""

class BaseGeometry:
    """
    BaseGeometry class.
    """

    def area(self):
        """
        Public instance method to calculate the area.

        Raises:
            Exception: Always raises an exception with the message 'area() is not implemented'.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Public instance method to validate an integer value.

        Parameters:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with given width and height.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        Public instance method to calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    Square class inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with the given size.

        Parameters:
            size (int): The size of the square.
        """
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)
