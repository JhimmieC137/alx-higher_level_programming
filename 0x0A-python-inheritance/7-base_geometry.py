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
    
    def integer_validator(self, name, value):
        """This method validates the arguments <name> and <value>

        Args:
            name(int)
            value(str)
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
