#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_key = ""
    best_value = 0
    for key in a_dictionary:
        if best_value < a_dictionary[key]:
            best_value = a_dictionary[key]
            best_key = key
    return best_key