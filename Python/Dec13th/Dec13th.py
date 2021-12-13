sampleInput = "Python\Dec13th\sample.txt"
puzzleInput = "Python\Dec13th\input.txt"

with open(sampleInput) as f:
    sample = f.readlines()

with open(puzzleInput) as f:
    puzzle = f.readlines()


def solveSample(myInput):
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

##################################

print(solveSample(sample))
