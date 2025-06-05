#!/usr/bin/python3
"""
This module allow to serialise and deserialize dats to xlm
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """serialize into xlm"""

    root = ET.Element("Data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """Deserialize from xlm"""
    my_dict = {}
    root = ET.parse(filename)
    
    start = root.getroot()
    for row in start:
        my_dict[row.tag] = row.text
    return my_dict