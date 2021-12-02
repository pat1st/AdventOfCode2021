import io

input = "Python\Dec2nd\input"   # "Python\Dec2nd\sample"
with open(input) as f:
    lines = f.readlines()

depth = horiz = aim = 0

for line in lines:
    (dir, val) = line.split()
    match dir:
        case "forward":
            horiz += int(val)
        case "up":
            depth -= int(val)
        case "down":
            depth += int(val)

print(depth, horiz, depth*horiz)

depth = horiz = aim = 0

for line in lines:
    (dir, val) = line.split()
    match dir:
        case "forward":
            horiz += int(val)
            depth += aim*int(val)
        case "up":
            #depth -= int(val)
            aim -= int(val)
        case "down":
            #depth += int(val)
            aim += int(val)

print(depth, horiz, depth*horiz)
