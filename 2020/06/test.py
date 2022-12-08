#!/usr/bin/env python3

# letters = []
# s = 0

# for line in open("in.txt"):
#     if line == "\n":
#         s += len(letters)
#         # print("adding",len(letters))
#         letters = []
#     else:
#         for l in line:
#             if l not in letters and l != '\n':
#                 # print("appending",l)
#                 letters.append(l)
# s += len(letters)
# # print("adding",len(letters))

# print("Silver:",s)



abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
s = 0
lines = []
for line in open("in.txt"):
    if line == "\n":
        letters = 0
        for l in abc:
            everywhere = True
            for ln in lines:
                if l not in ln:
                    everywhere = False
            if everywhere:
                print(l,'is everywhere')
                letters += 1
        print('adding',letters)
        s += letters
        lines = []

    else:
        lines.append(line)

letters = 0
for l in abc:
    everywhere = True
    for ln in lines:
        if l not in ln:
            everywhere = False
    if everywhere:
        print(l,'is everywhere')
        letters += 1
s+=letters
print('adding',letters)

# print("adding",len(letters))

print("Gold:",s)
