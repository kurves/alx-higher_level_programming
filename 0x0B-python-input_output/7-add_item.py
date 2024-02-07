#!/usr/bin/python3
"""function to load from json"""

import json
import sys
from os.path import exists

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    def add_items_and_save(arguments):    
        """function to load json"""
        if exists("add_item.json"):
            items = load_from_json_file("add_item.json")
        else:
            items = []
        items.extend(arguments)
        save_to_json_file(items, "add_item.json")
