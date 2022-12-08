claims = []

# create an array of dictionares
with open('data03.txt') as f:
    for line in f:
        part1 = line.partition('@')[0]
        part2 = line.partition('@')[2].partition(':')[0]
        part3 = line.partition(':')[2]

        claim = {'id':0, 'start':(0,0), 'size':(0,0)}
        claim['id'] = int(part1[1:])
        claim['start'] = [int(part2.partition(',')[0]),
                int(part2.partition(',')[2])]
        claim['size'] = [int(part3.partition('x')[0]) , 
                int(part3.partition('x')[2])]
        claims.append(claim)


# create matrix 1000x1000 filled with 0
matrix = []
for i in range(1000):
    matrix.append([])
    for j in range(1000):
        matrix[i].append(0)

#add 1 to the cell each time it is covered
for claim in claims:
    y,x = claim['start']
    h,w = claim['size']
    for i in range(h):
        for j in range(w):
            matrix[x+j][y+i] += 1

# check the id of the area that isn't overlapped
for claim in claims:
    overlaps = False
    y,x = claim['start']
    h,w = claim['size']
    for i in range(h):
        for j in range(w):
            if matrix[x+j][y+i] != 1:
                overlaps = True
    if not overlaps:
        print(claim['id'])

# count overlapped area
count = 0
for i in matrix:
    for j in i:
        if j > 1:
            count += 1
print('Area overlaped by at least 2:', count)

