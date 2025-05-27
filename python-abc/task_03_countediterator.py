#!/usr/bin/python3
"""
This module...
"""


class CountedIterator():
    """
    this class...
    """
    def __init__(self, item):
        """
        Init the counter iterator
        """
        self.item = item
        self.iterator = iter(item)
        self.count = 0

    def get_count(self):
        """
        Allow to know the current iteration
        """
        return self.count

    def __iter__(self):
        """
        Return self
        """
        return self

    def __next__(self):
        """
        return the next item and icrement count
        """
        if self.count <= len(self.item):
            val = next(self.iterator)
            self.count += 1
            return val
        else:
            raise StopIteration
