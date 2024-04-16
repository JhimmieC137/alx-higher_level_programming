#!/usr/bin/python3
"""This python document returns a boolean on confimation of an object type"""


def is_same_class(obj, a_class):
    """This function checks if an object is the instance of a class
    Args:
        obj (any): An object
        a_class (any): A class
    Return:
        boolean
    """
    return type(obj) is a_class
