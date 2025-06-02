#!/usr/bin/python3
"""
This module is an object that need to be returned for a json serialization
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

    def to_json(self):
        """
        This function return a dict of object for a json serialization
        """
        return self.__dict__
