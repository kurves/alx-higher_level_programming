#!/usr/bin/python3
"""function to convert data"""

import json


def from_json_string(my_str):
    """function to convert data"""
    data = json.loads(my_str)
    return data
