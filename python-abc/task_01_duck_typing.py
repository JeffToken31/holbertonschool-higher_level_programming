#!/usr/bin/python3
"""
This module use duck typing concept to create subclasses and adapted methods
"""


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Mother class to def methods for subclasses
    """
    @abstractmethod
    def area(self):
        """
        Method who allow to calcul area of childrens classes
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Method who allow to calcul perimeter of childrens classes
        """
        pass


class Circle(Shape):
    """
    Circular object class
    """
    def __init__(self, radius=0):
        """
        Inicialize a Rectancle
        """
        self.radius = radius

    def area(self):
        """
        Define area of a circle
        """
        return (self.radius * self.radius) * pi

    def perimeter(self):
        """
        Define area of a circle
        """
        return (2 * self.radius) * pi


class Rectangle(Shape):
    """
    Rectancle object class
    """
    def __init__(self, width=0, height=0):
        """
        Inicialize a Rectancle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Define area of a rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Define area of a rectangle
        """
        return (self.width * 2) + (self.height * 2)


def shape_info(obj):
    """
    Keep info of method area and perimeter
    """
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
