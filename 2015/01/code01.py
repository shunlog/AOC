with open('data01.txt') as f:
    text = f.read()
print(text)

floor = 0
count = 1
for i in text:
    if i == '(':
        floor += 1
    elif i == ')':
        floor -= 1
    if floor == -1:
        break
    count += 1
print('part one:',floor)
print('part two:', count)
