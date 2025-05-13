#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best = 0
    for i in a_dictionary.values():
        if i > best:
            best = i
    dict_filtered = dict(filter(lambda x: x[1] == best, a_dictionary.items()))

    return dict_filtered
