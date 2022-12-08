#!/usr/bin/env python3

ls = []
with open("in.txt","r") as f:
    f.readline()
    s = f.readline()[:-1].split(',')

    bi = 0
    for n in s:
        if n.isdigit():
            ls.append([bi,int(n)])
        bi += 1

    print(ls)

def xi(Ni,ni):
    if Ni == 0 or ni == 0:
        return 0
    xi = 0
    while Ni*xi % ni != 1:
        xi += 1
    return xi


# ls is a list of pairs
# a pair is [bi, ni] where bi - remainder, ni - divisor
def chinese(ls):
    N = 1
    for pair in ls:
        N *= pair[1]

    S = 0
    for pair in ls:
        bi = pair[0]
        ni = pair[1]
        Ni = N/ni
        prod = bi * Ni * xi(Ni,ni)
        S += prod
    return int(S)

print(chinese(ls))
