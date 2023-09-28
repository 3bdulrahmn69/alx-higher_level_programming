#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """function that finds a peak in a list"""
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    x = int(length / 2)
    loi =list_of_integers

    if x - 1 < 0 and x + 1 >= length:
         return loi[x]
    elif x - 1 < 0:
        return loi[x] if loi[x] > loi[x + 1] else loi[x + 1]
    elif x + 1 >= length:
        return loi[x] if loi[x] > loi[x - 1] else loi[x - 1]

    if loi[x - 1] < loi[x] > loi[x + 1]:
        return loi[x]

    if loi[x + 1] > loi[x - 1]:
        return find_peak(loi[x:])
    return find_peak(loi[:x])
