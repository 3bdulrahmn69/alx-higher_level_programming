#!/usr/bin/python3
"""
module that contains a class that inherits from list
"""


class MyList(list):
    """a class that inherits from list"""
    def __init__(self):
        """initializes"""
        super().__init__()
    
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))