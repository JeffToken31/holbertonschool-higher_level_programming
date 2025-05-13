#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dict = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100,  'XC': 90,  'L': 50,  'XL': 40,
        'X': 10,   'IX': 9,   'V': 5,   'IV': 4,
        'I': 1
    }
    number = 0
    i = 0
    while i < len(roman_string):
        if i + 1 < len(roman_string):
            pair = roman_string[i] + roman_string[i + 1]
            if pair in roman_dict:
                number += roman_dict[pair]
                i += 2
                continue

        number += roman_dict[roman_string[i]]
        i += 1
    return number
