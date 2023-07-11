#!/usr/bin/python3
"""
a module that contains a class Student
"""


class Student:
    """a class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method that retrieves a dictionary representation"""
        return self.__dict__
