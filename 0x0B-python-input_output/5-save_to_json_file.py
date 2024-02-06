#!/usr/bin/python3
"""function to save object"""

import json


def save_to_json_file(my_obj, filename):
	"""save to file function"""
	with open(filename, "w") as file:
		data = json.dump(my_obj, file)
	return data
