#!/usr/bin/python3
"""
This module...
"""


class CountedIterator():
    """
    this class...
    """
    def __init__(self, item):
        self.item = item
        self.iterator = iter(item)
        self.count = 1

    def get_count(self):
        return self.count

    def __next__(self):
        if self.count < len(self.item):
            val = next(self.iterator)
            self.count += 1
            return val
        else:
            raise StopIteration
