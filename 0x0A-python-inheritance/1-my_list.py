#!/usr/bin/python3
"""
A module for sorting lists.
"""


class MyList(list):
    """
    A blue print for customizing a sorted list.
    """
    def __init__(self):
        """
        Initialize the blueprint.
        """
        super().__init__(self)

    def print_sorted(self):
        """
        Sorts a list in ascending order.
        """
        new_list = sorted(self)
        print(new_list)
