#!/usr/bin/python3
"""
function that prints a text with 2 new lines after each of these characters: ., ? and :
"""
def text_indentation(text):
    """ function that prints a text with 2 new lines after each of these characters: ., ? and : """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in text:
        if i in [".", "?", ":"]:
            print(i, end="")
            print("")
            print("")
        else:
            print(i, end="")
