#!/usr/bin/python3
"""
This module allow us to understand mixin methods
"""
class Fish:
    """
    A maritim class
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

class Bird:
    """
    An aerian class
    """
    def fly(self):
        print("The bird is flying")
    
    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """
    class with multiples parents
    """
    def fly(self):
        print("The flying fish is soaring!")
    
    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")