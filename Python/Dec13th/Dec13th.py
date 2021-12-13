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
            x, y = getCoord(coord)
            coords.append([x, y])

        if 'fold' in coord:
            if 'x' in coord:
                x = int(coord.split('=')[1])
                instructions.append(['x', x])
            if 'y' in coord:
                y = int(coord.split('=')[1])
                instructions.append(['y', y])

    return coords, instructions

def getCoord(coord):
    xy = coord.strip().split(',')
    x = int(xy[0])
    y = int(xy[1])
    return x,y


def fold(coords, direction, value):
    newCoords = []
    for actual in coords:
        x, y = getCoord(actual)
        if direction=='y':
            if y > value:
                y = y - (value - y)
        if direction=='x':
            if x > value:
                x = x - (value - x)
        if 1==1:
            newCoords.append([x, y])

    return newCoords



##################################

print(readInputData(sample))
