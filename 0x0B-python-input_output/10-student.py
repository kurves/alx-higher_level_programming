#!/usr/bin/python3
"""class student"""


class Student:
    """class defintion"""
    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance."""
        if attrs is None:
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age,
            }
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
