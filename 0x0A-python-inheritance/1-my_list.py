#!/usr/bin/python3
import doctest

"""This python document returns a list"""


class MyList(list):
    """A class that inherits from the built in list class"""

    def print_sorted(self):
        """This method priints the sorted form of the initialized list"""
        sim = self.copy()
        sim.sort()
        print(sim)


if __name__ == "__main__":
    doctest.testfile("tests/1-my_list.txt")
