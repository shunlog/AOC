#!/usr/bin/env python
from tqdm import tqdm
'''
Horrible, takes like 25 minutes to complete
I create a list of [x, y, len] for each wire and then find the intersections
then i iterate the intersections to find the smallest distance and length

There must be a faster way
'''

# a Posn is a list
# [Number, Number]
# interpretation: x and y coordinates

# Posn, Posn -> Posn
def add_posn(p1, p2):
    return [p1[0] + p2[0], p1[1] + p2[1]]

# String -> [List-of Posn]
# Return the list of all positions the wire traverses
def get_coords_list(s):
    moves = s.split(',')
    pos = [0, 0, 0]
    coords = []
    steps = 0

    for m in moves:
        if m[0] == 'R':
            dir = [1, 0]
        elif m[0] == 'U':
            dir = [0, -1]
        elif m[0] == 'L':
            dir = [-1, 0]
        elif m[0] == 'D':
            dir = [0, 1]
        for count in range(int(m[1:])):
            pos = add_posn(pos, dir)
            steps += 1
            pos.append(steps)
            coords.append(pos)
    return coords


# [X, Y, Number], [X, Y, Number] -> bool
# return the coord and len of second wire from the list if it has the same coord as posn p1
# else False
def eq_coords(p1, p_ls):
    for p2 in p_ls:
        if p1[0] == p2[0] and p1[1] == p2[1]:
            return p2
    return False

# [List-of Posn], [List-of Posn] -> [List-of Posn]
def get_intersections(posn_ls1, posn_ls2):
    intersections = []
    for p in tqdm(posn_ls1):
        p2_inter = eq_coords(p, posn_ls2)
        # if there is a coord the second wire also traverses
        if p2_inter:
            len_sum = p2_inter[2] + p[2]
            p.pop()
            p.append(len_sum)
            intersections.append(p)
    return intersections

# Posn -> Number
# get manhattan distance from origin (0, 0) to posn
def get_manhattan_dist(posn):
    return abs(posn[0]) + abs(posn[1])


with open("test3.txt", 'r') as f:
    steps1 = f.readline()
    steps2 = f.readline()

wire1 = get_coords_list(steps1)
wire2 = get_coords_list(steps2)



inters = get_intersections(wire1, wire2)
print("Intersections:",inters)

dist_ls = []
len_ls = []

for inter in inters:
    # part 1
    dist_ls.append(get_manhattan_dist(inter))
    # part 2
    len_ls.append(inter[2])

print("Min manhattan distance:", min(dist_ls))


print("Min length sum:",min(len_ls))
