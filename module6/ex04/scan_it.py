#! /usr/bin/env python3

import re
import sys

if len(sys.argv) != 3:
    print("none")
    exit()

numbers = sys.argv[1]
strings = sys.argv[2]

all_words = re.findall(numbers, strings)

if len(all_words) == 0:
    print("none")
    exit()

print(len(all_words))