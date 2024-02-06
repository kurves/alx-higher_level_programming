#!/usr/bin/python3
"""function that appends from stdin"""

def append_write(filename="", text=""):
    """function to read file"""
    try:
        with open(filename, 'a') as f:
            data = f.write(text)
            return data
    except:
        return 0
