#!/usr/bin/python3

"""base claSS defintion"""
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string."""

        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
