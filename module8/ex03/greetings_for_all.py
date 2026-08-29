#!/usr/bin/env python3

import sys

def greetings(txt = "mobile stranger"):
    if type(txt) is not str:
        print("error! It was not a name.")
    else:
        print("Hello, " + txt + "!")

greetings("Alexandra")
greetings("Wil")
greetings()
greetings(42)