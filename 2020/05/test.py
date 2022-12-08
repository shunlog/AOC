#!/usr/bin/env python3

maxID = 0

seats = list(range(128*8+8))
for line in open("in.txt", 'r'):
    row = int(line[:7].replace('B','1').replace('F','0'), 2)
    col = int(line[7:].replace('R','1').replace('L','0'), 2)
    ID = row * 8 + col
    seats.remove(ID)
    maxID = max(ID, maxID)

print("Silver:",maxID)
print("Gold:",seats)
