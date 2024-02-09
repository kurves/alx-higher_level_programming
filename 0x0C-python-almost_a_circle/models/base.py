#!/usr/bin/python3

"""base claSS defintion"""

class Base:
    """class defining a class"""
     __nb_objects = 0

    def __init__(self, id=None):
    """defining id attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
