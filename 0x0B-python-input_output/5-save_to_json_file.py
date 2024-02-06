#!/usr/bin/python3
import json
"""function to save object"""

def save_to_json_file(my_obj, filename):
    try:
        with open(filename, "w") as file:
            data = json.dump(my_obj, file)
            return data
    except:
        pass
