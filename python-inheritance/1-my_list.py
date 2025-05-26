#!/usr/bin/python3
"""
This module allow to print a sorted list
"""


class MyList(list):
    """
    Children class of list
    """
    def print_sorted(self):
        """
        Print a copy of sorted list of his parent
        """
        copy = self[:]
        copy.sort()
        print(copy)
