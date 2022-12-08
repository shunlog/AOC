with open('data05.txt') as f:
    str = f.read()
print(len(str))
   
def react(str):
    while True:
        no_changes = True
        for i in range(len(str)):
            try:
                a = str[i]
                b = str[i+1]
                if a.upper() == b.upper() and a != b:
                    str = str.replace(a+b, '', 1)
                    no_changes = False
                    break
            except:
                break
        if no_changes:
            break
    return str

str = react(str)
print("Part one:",len(str))

letters = [chr(i) for i in range(97,123)]

min_len = len(str)
for letter in letters:
    new_str = ''
    for i in range(len(str)):
        if str[i].lower() != letter:
            new_str += str[i]
    new_str = react(new_str)
    print(letter, len(new_str))
    if len(new_str) < min_len:
        min_len = len(new_str)
        letter_to_remove = letter
            
print(letter_to_remove, min_len)
