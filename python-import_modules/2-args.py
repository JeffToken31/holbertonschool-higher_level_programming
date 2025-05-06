#!/usr/bin/python3
from sys import argv

print(f"{len(argv) - 1} arguments:")
for i in range(len(argv) - 1):
    print(f"{i + 1}: {argv[i + 1]}")
