arr = []
ls = []
sum = 0
with open('data01.txt') as f:
    for line in f:
        try:
            ls.append(int(line))
        except:
            pass

found = False
while True:
    for freq in ls:
        sum+= freq
        if sum in arr:
            print(sum)
            found = True
            break
        else:
            arr.append(sum)
    if found:
        break
