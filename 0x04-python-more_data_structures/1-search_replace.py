#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n = my_list.copy()
    for i in range(len(n)):
        if n[i] == search:
            n[i] = replace
    return n
