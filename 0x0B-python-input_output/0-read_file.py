#!/usr/bin/python3
"""function that reads from stdin"""

def read_file(filename=""):
	"""function to read file"""
	with open(filename, 'r', encoding="utf-8") as f:
        	sentences = f.read()
	        print(sentences, end="")
