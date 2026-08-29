#! /usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("none")
else:
    print("parameters:", len(sys.argv) - 1)

    for parameter in sys.argv[1:]:
        print(parameter + ":", len(parameter))