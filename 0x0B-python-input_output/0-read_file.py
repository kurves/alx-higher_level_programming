#!/usr/bin/python3
"""function that reads from stdin"""

def read_file(filename=""):
    """function to read file"""
    with open(filename, 'r') as f:
        sentences = f.read()
        print(sentences)
