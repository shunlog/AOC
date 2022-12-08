import re
with open('data10.txt') as f:
    data = []
    lines = f.readlines()
    for line in lines:
        # extract all numbers consecutively
        data.append(re.findall("[^a-z=<>\n' ',]+", line))


