#!/usr/bin/env python3

grammar = []

with open('test.txt') as f:
    for line in f:
        if line == '\n':
            break
        rn, expr = [x.strip() for x in line.split(':')]
        grammar.append((int(rn), expr))

print(grammar)

# procedure bt(c) is
#     if reject(P, c) then return
#     if accept(P, c) then output(P, c)
#     s ← first(P, c)
#     while s ≠ NULL do
#         bt(s)
#         s ← next(P, s)
