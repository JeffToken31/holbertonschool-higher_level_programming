#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    filted_list = set(my_list)

    for element in filted_list:
        result += element
    return result
