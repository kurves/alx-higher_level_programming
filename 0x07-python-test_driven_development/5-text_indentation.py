#!/usr/bin/python3

"""
function to print lines
raises: typeerror
returns str
"""

def text_indentation(text):
    """
    function that identation to text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = "" 
    for char in text:
        result += char
        if char in ('.', ':', '?'):
            result += "\n\n"
    print(result.strip())
