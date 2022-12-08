ls = []
with open('data02.txt') as f:
    for line in f:
        ls.append(line)

times_two = times_three = 0

for line in ls:
    letters = []
    count = {}
    for let in line:
        if let in letters:
            count[let] += 1
        else:
            letters.append(let)
            count[let] = 1
    for i in count:
        if count[i] == 2:
            times_two += 1
            break
    for i in count:
        if count[i] == 3:
            times_three += 1
            break
checksum = times_two * times_three

# part 2 - check for two strings that differ only by a char

def contains_twice(s, arr, i):
    count = 0
    for j in range(len(arr)):
        if s == arr[j][:i] + arr[j][i+1:]:
            count += 1
    if count == 2:
        return True
    return False

for i in range(27):
    for l in range(len(ls)):
        s1 = ls[l][:i] + ls[l][i+1:]
        if contains_twice(s1, ls, i):
            print(s1)







