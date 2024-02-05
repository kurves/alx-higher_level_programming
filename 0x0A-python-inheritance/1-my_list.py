#!/usr/bin/python3

"""
class that inherits from another class
"""

class MyList(list):
    """
    MyList class inherits from list.
    """

    def print_sorted(self):
        """
        Public instance method to print the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
