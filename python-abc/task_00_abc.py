#!/usr/bin/python3
from abc import ABC, abstractmethod
"""
This module use abstract class to create subclass
"""
class Animal(ABC):
    """
    Abstract class allow subclasses generique methodes
    """
    @abstractmethod
    def sound(self):
        """
        Generic method for all animals
        """
        pass

class Dog(Animal):
    """
    Class of dog
    """
    def sound(self):
        """
        Sound of the dogs
        """
        return "Bark"
    
class Cat(Animal):
    """
    Class of cat
    """
    def sound(self):
        """
        Sound of the cats
        """
        return "Meow"