#!/usr/bin/python3
"""This python document returns a boolean on confimation of an object type"""


def inherits_from(obj, a_class):
    """This function checks if an object is the instance of a class
    Args:
        obj (any): An object
        a_class (any): A class
    Return:
        boolean
    """
    if type(obj) == a_class:
        return False
    else:
        return issubclass(type(obj), a_class) 
