#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""This is a script containing the rectangle class"""


class Rectangle(BaseGeometry):
    """The Rectangle class inherits from BaseGeometry but
        has private attributes width and height as an update
    """
    def __init__(self, width, height):
        """Initializing the class so we can define attributes"""
        if super().integer_validator("width", width):
            self.__width = width
        if super().integer_validator("height", height):
            self.__height = height
