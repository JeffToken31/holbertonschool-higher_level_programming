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
        good_order = ["age", "last_name", "first_name"]
        if attrs is None:
            for key in good_order:
                new_dict[key] = self.__dict__[key]
            return new_dict

        for attr in attrs:
            if type(attr) is str:
                if hasattr(self, attr):
                    new_dict[attr] = getattr(self, attr)

        sorted_dict = {}
        for key in sorted(new_dict):
            sorted_dict[key] = new_dict[key]
        return sorted_dict

    def reload_from_json(self, json):
        """
        This public method replaces all attributes of the Student instance
        """
        for key in json:
            self.__dict__[key] = json[key]
