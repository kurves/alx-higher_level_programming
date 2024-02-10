#!/usr/bin/python3
"""defining the Square class."""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Defines a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
