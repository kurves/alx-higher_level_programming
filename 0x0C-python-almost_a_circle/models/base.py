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

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode='w') as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))
