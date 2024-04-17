#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""This is a script containing the rectangle class"""


class Rectangle(BaseGeometry):
    """The Rectangle class inherits from BaseGeometry but
        has private attributes width and height as an update
    """
    def __init__(self, width, height):
        """Initializing the class so we can define attributes as private"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Check if width is a valid integer"""
        super().integer_validator("width", width)
        return self.__width

    @property
    def height(self):
        """Check if height is a valid integer"""
        super().integer_validator("height", height)
        return self.__height
