#!/usr/bin/env python3

import sys

def shrink(string):
    print(string[:8])


def enlarge(string):
    while len(string) < 8:
        string += "Z"
    print(string)


for argument in sys.argv[1:]:
    if len(argument) > 8:
        shrink(argument)
    elif len(argument) < 8:
        enlarge(argument)
    else:
        print(argument)
