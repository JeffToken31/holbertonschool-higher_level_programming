#!/usr/bin/python3
from abc import ABC, abstractmethod
"""
This module use duck typing concept to create subclasses and adapted methods
"""
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