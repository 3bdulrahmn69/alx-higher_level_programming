#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    else:
        roman_dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        decs = [roman_dic[x] for x in roman_string]
        converts  = 0
        for i in range(len(decs)):
            converts += decs[i]
            if decs[i - 1] < decs[i] and i != 0:
                converts -= (decs[i - 1] + decs[i - 1])
        return converts
