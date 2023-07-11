#!/usr/bin/python3
"""
a module that have a function that writes a string to a text file and returns the number of characters written
"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        f.closed
    return(len(text))
