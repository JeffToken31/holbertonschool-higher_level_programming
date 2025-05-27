#!/usr/bin/python3
"""
This module
"""


class VerboseList(list):
    """
    Children class of list
    """
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        idx = super().pop(index)
        print("Popped [{}] from the list.".format(idx))
        return idx
