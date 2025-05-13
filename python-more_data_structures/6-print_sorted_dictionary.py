#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dico = dict(sorted(a_dictionary.items(), key=lambda x: x))
    for key in sorted_dico:
        print("{}: {}".format(key, sorted_dico[key]))
