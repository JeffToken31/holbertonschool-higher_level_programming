#!/usr/bin/python3
"""
This module provide a class which will be returned in dict with filters
"""


class Student:
    """
    This class keep information from student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialisation of object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This function return a dict of object
        with attributs desired for a json serialization
        """
        new_dict = {}
        if attrs is None:
            return self.__dict__
        for attr in attrs:
            if type(attr) is str:
                if hasattr(self, attr):
                    new_dict[attr] = getattr(self, attr)
        return new_dict
