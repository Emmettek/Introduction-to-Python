#! /usr/bin/env python3

number = float(input("Give me a number: "))
# print(number % 1)

if number % 1 == 0:
    print("This number is an integer.")
else:
    print("This number is a decimal.")