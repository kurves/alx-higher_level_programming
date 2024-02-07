#!/usr/bin/python3
"""function to return json object"""


def class_to_json(obj):
    """Returns a dictionary data structures for JSON."""
    json_dict = {}
    obj_dict = obj.__dict__
    for attr, value in obj_dict.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value

    return json_dict
