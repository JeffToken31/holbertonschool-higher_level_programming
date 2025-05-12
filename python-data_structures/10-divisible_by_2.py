#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    checked = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            checked.append(True)
        else:
            checked.append(False)
    return checked
