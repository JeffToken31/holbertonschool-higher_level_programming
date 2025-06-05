#!/usr/bin/python3
"""
This module can convert data in csv into json
"""
import json
import csv


def convert_csv_to_json(filename):
    """
    Function to convert data.csv into json format
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            new_dict = csv.DictReader(f)
            new_data = list(new_dict)
    except FileNotFoundError:
        return False

    try:
        with open("data.json", "w", encoding="utf-8") as fj:
            json.dump(new_data, fj)
        return True
    except FileNotFoundError:
        return False
