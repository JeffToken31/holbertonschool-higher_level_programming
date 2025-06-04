#!/user/bin/python3
"""
This module provide a class with serialization methods
"""
import pickle


class CustomObject:
    """
    This class is created to use serialization
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}\nAge: {}\nIs Student: {}\n"
              .format(self.name, self.age, self.is_student))

    def serialize(self, filename):
        """
        This function serialize into pickle an object
        """
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        This class method is to deserialize into new instance
        """
        with open(filename, "rb") as f:
            return pickle.load(f)
