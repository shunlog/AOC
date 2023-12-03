#!/usr/bin/env python3
from icecream import ic

storage = {}
def process_input_line(line):
    ic(line)
    line = line.strip()
    line = [s.replace(",", "").replace(":", "") for s in line.split(" ")]
    n = 1
    storage[line[1]] = {}
    storage[line[1]][str(n)] = {}
    for i in range(2, len(line), 2):
        if line[i + 1] not in storage[line[1]][str(n)]:
            storage[line[1]][str(n)][line[i+1]] = int(line[i])
        if ";" in line[i + 1]:
            storage[line[1]][str(n)][line[i+1].replace(";", "")] = int(line[i])
            del storage[line[1]][str(n)][line[i+1]]
            n += 1
            storage[line[1]][str(n)] = {}

    ic(line)

def solver():
    ic(storage)
    counter = 0
    for id in storage.keys():
        red = 0
        green = 0
        blue = 0
        for game_set in storage[id].keys():

            for col in ['red', 'green', 'blue']:
                if col not in storage[id][game_set]:
                    storage[id][game_set][col] = 0

            power = 0

            if storage[id][game_set]['red'] > red:
                red = storage[id][game_set]['red']
            if storage[id][game_set]['blue'] > blue:
                blue = storage[id][game_set]['blue']
            if storage[id][game_set]['green'] > green:
                green = storage[id][game_set]['green']

        counter += (green * blue * red)
    print(counter)

file_path = 'input.in'
try:
    with open(file_path, 'r') as file:
        # Or read all lines into a list
        lines = file.readlines()
        for line in lines:
            process_input_line(line)
        solver()
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
