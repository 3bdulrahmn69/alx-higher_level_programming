#!/usr/bin/python3
"""
a module that have a function that reads a text file and prints it to stdout
"""


def read_file(filename=""):
    """a function that reads a text file"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
