#!/usr/bin/python3
import json
"""function to load from json"""

def load_from_json_file(filename):
    """function to load json"""
    with open(filename, "r") as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError:
            return None
