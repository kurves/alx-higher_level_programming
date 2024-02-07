#!/usr/bin/python3
"""function that reads from stdin"""


def write_file(filename="", text=""):
    """function to read file"""
        with open(filename, 'w', encoding="utf-8") as f:
            data = f.write(text)
        return data
