#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        b = sorted(a_dictionary.values())
        return b[-1]
