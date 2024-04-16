#!/usr/bin/python3
"""This script contains class with methods"""


class BaseGeometry():
    """BaseGeometry
        This is a subclass of the BaseGeometry class
    """
    def area(self):
        """This mther argument other than the reference self
            and raises and exeption
            Args:
               self(None)
            Returns:
                None
        """
        raise Exception("area() is not implemented")
