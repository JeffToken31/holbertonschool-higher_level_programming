#!/usr/bin/python3
"""
This module allow to serialise and deserialize dats to xlm
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """serialize into xlm"""

    with