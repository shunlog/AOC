import re

data = []
with open('data07.txt') as f:
    for line in f:
        letters = re.findall(r'[A-Z]\b', line)
        data.append(letters)

requirements = {}
for i in data:
    if i[1] not in requirements:
        requirements[i[1]] = list(i[0])
    else:
        requirements[i[1]].append(i[0])

data.sort()
parent_nodes = []
children_nodes = []
for i in data:
    parent_nodes += i[0]
    children_nodes += i[1]

root_nodes = sorted(list(set(parent_nodes) - set(children_nodes)))
terminal_nodes = sorted(list(set(children_nodes) - set(parent_nodes)))


available = list(root_nodes)
instructions = ''
nodes_met = []

def prerequisites_met(nodes_met, node):
    for i in data:
        if i[1] == node:
            if i[0] not in nodes_met:
                return False
    return True

while True:
    available.sort()
    try:
        node = available[0]
    except:
        break
    instructions += node
    nodes_met += node
    for i in data:
        if i[0] == node and i[1] not in available: 
            if prerequisites_met(nodes_met, i[1]):
                available += i[1]
    available = available[1:]
            

print('Part one:',instructions)


def set_time(node):
    letters = [chr(i) for i in range(97,123)]
    for i in range(26):
        if node.lower() == letters[i]:
            return 61 + i

def requirements_met(node, done):
    try:
        for i in requirements[node]:
            if i not in done:
                return False
    except:
        pass
    return True


done = ''
operations = []
for i in range(5):
    operations.append(['', 0])
time = 0
final_length = len(instructions)

while True:
    for op in operations:
        
        if op[0] != '' and op[1] == 0: # if worker has finished
            done += op[0]
            op[0] = ''
            #print(op[0], 'has finished')

        if op[0] == '': # worker has no job
            if len(instructions) == 0:
                continue
            for instr in instructions:
                if not requirements_met(instr, done): # this job can't be done yet
                    continue
                op[1] = set_time(instr)
                op[0] = instr
                instructions = instructions.replace(instr, '')
                break

        if op[0] != '' and op[1] != 0: # if worker is working
            op[1] -= 1
    time += 1
    if len(done) == final_length:
        break

print('Part two:',time)
            



