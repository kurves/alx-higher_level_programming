#!/usr/bin/python3

"""base claSS defintion"";wq



class Square:
    """class defining a class"""
    def __init__(self, size=0, position=(0,0)):
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
