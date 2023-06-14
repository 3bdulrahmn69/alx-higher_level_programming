#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        b = sorted(a_dictionary.values())

        key_list = list(a_dictionary.keys())
        val_list = list(a_dictionary.values())
        position = val_list.index(b[-1])

        return key_list[position]
    else:
        return None
