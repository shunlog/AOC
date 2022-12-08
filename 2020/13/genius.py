#!/usr/bin/env python3

import sys

file = open(sys.argv[1], 'r')
lines = file.readlines()

timestamp = int(lines[0])
busIDs = [(-y, int(d)) for y, d in enumerate(lines[1].split(',')) if d.rstrip('\r\n') != 'x']

file.close()

# Part 1

arrivals = [(i, (i - (timestamp % i))) for y, i in busIDs]

minID, minTime = arrivals[0]
for ID, time in arrivals:
  if (time < minTime):
    minID, minTime = ID, time

print(f'Part 1: {minID * minTime}')

# Part 2

def mult_inv(a, b):
  b0 = b
  x0, x1 = 0, 1

  if (b == 1):
    return 1
  while (a > 1):
    q = a // b
    a, b = b, a % b
    x0, x1 = x1 - q * x0, x0
  if (x1 < 0):
    x1 += b0
  return x1

# Chink Remainder Theorem

x, M = 0, 1
for y, d in busIDs:
  M *= d

for y, d in busIDs:
  b = M // d
  x += b * y * mult_inv(b, d)

print(f'Part 2: {x % M}')
