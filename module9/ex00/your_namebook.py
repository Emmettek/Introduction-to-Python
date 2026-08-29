#!/usr/bin/env python3

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

def array_of_names(dictory):
    array = []
    for str in dictory:
        first = str.capitalize()
        last = dictory[str].capitalize()
        array.append(first + " " + last)
    
    return array

    
print(array_of_names(persons))