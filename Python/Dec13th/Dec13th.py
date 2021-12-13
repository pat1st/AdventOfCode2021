from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt

sampleInput = "Python\Dec13th\sample.txt"
puzzleInput = "Python\Dec13th\input.txt"

with open(sampleInput) as f:
    sample = f.readlines()

with open(puzzleInput) as f:
    puzzle = f.readlines()


def readInputData(myInput):
    lines = list(myInput)
    coords = []
    instructions = []

    for coord in lines:

        if coord.strip() == "":
            continue

        if ',' in coord:
            xy = coord.strip().split(',')
            x = int(xy[0])
            y = int(xy[1])
            coords.append([x, y])

        if 'fold' in coord:
            if 'x' in coord:
                x = int(coord.split('=')[1])
                instructions.append(['x', x])
            if 'y' in coord:
                y = int(coord.split('=')[1])
                instructions.append(['y', y])

    return coords, instructions


def fold(coords, direction, value):
    newCoords = []
    for actual in coords:
        x = int(actual[0])
        y = int(actual[1])

        if direction == 'y':
            if y >= value:
                y = y - 2*(y-value)
        if direction == 'x':
            if x >= value:
                x = x - 2*(x-value)
        if [x, y] in newCoords:
            # do nothing
            i = 1
        else:
            newCoords.append([x, y])

    return newCoords


##################################
coords, instructions = readInputData(puzzle)
print(coords, len(coords))
print(instructions)

plt.scatter(*zip(*coords))
beforfolded = coords

counter = 0
for instruction in instructions:
    direction = instruction[0]
    amount = instruction[1]
    print(direction, amount)

    if counter != 0:
        beforfolded = folded
    folded = fold(coords, direction, amount)
    
    if direction == 'y':
        plt.axhline(y=amount, linestyle='-', label=counter)
    if direction == 'x':
        plt.axvline(x=amount, linestyle='-', label=counter)

    plt.scatter(*zip(*beforfolded))
    plt.scatter(*zip(*folded))
    
    counter = counter+1
    plt.show()

plt.show()
