#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        re = (0, None)
        return re
    else:
        re = (len(sentence), sentence[0:1])
        return re
