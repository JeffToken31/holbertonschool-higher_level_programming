#!/usr/bin/python3
"""
This module use mixin methode
"""


class SwimMixin:
    """
    Class to call if creature is swimming
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Class to call if creature is flying
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Children class of multiple parents
    """
    def swim(self):
        return super().swim()

    def fly(self):
        return super().fly()

    def roar(self):
        print("The dragon roars!")
