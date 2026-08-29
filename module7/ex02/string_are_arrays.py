#! /usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    string = sys.argv[1]
    count = 0

    for char in string:
        if char == "z":
            print("z", end="")
            count += 1

    if count == 0:
        print("none")
    else:
        print()