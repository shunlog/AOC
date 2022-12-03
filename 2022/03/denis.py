#!/usr/bin/env python3

f =  open("input.txt", 'r')
lines = f.readlines()

import string
alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)

summ = 0
for index in range(0, len(lines), 3):
    bags = [lines[index].strip(), lines[index + 1].strip(), lines[index + 2].strip()]
    # bags = [l.strip() for l in lines[index:index+3]]
    for item in bags[0]:
        if item in bags[1] and item in bags[2]:
            summ += alphabet.index(item, 0, len(alphabet)) + 1
            break

print(summ)
