#!/usr/bin/python3
"""function to convert data"""

import json


def to_json_string(my_obj):
    """function to convert data"""
    data = json.dumps(my_obj)
    return data

