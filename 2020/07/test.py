#!/usr/bin/env python3

FN = "in.txt"
MY_BAG = "shiny gold"
# bag is a dict:
# color -> string, the key
# num -> integer
# bags -> tuple denoting the (color,count) of bags it can hold

# bags is an array of bag
bags = []

for line in open(FN):
    bag = {}
    contents = {}

    line = line.replace('bags', 'bag').split('bag')
    color = line[0].strip()

    if "other" not in line[1]:
        for k in line[1:-1]:
            l = k.strip().split()
            num = int(l[1])
            col = ' '.join(l[2:])
            contents[col] = num

    bag['color'] = color
    bag['contents'] = contents
    bags.append(bag)

# for bag in bags:
#     print(bag)

good_bags = []
for bag in bags:
    for color in bag['contents']:
        if color == MY_BAG:
            good_bags.append(bag['color'])

added = True
while added:
    added = False
    for bag in bags:
        if bag['color'] in good_bags:
            continue
        for gbag in good_bags:
            for color in bag['contents']:
                if gbag == color:
                    added = True
                    good_bags.append(bag['color'])
                    break
            if added:
                break

print('Silver:',len(good_bags))

def sum_bags(color):
    sum = 1
    for bag in bags:
        if bag['color'] != color:
            continue
        if bag['contents'] == {}:
            continue
        for cont in bag['contents']:
            sum += bag['contents'][cont] * sum_bags(cont)
    return sum

sum = sum_bags('shiny gold') - 1
print('Gold:',sum)
