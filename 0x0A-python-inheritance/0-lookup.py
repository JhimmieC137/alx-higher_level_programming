#!/usr/bin/python3
"""This python script returns a list of methods within a given class"""


def lookup(obj):
    """The lookup function takes in a class or class
        object and return a list of contained methods

    Args
        <class> obj
    Returns
        <list>
    """
    return list(dir(obj))
