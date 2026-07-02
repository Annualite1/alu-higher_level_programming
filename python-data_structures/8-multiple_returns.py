#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple: (length of string, first character)."""
    if sentence == "":
        return (0, None)

    return (len(sentence), sentence[0])
