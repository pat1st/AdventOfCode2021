from matplotlib import colors
from matplotlib.patches import Rectangle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

tx1 = 20
tx2 = 30
ty1 = -10
ty2 = -5

vx = 0
vy = 0
maxy = 0


def checkIfTargetReached(px, py):
    if (tx1 <= px <= tx2) or (tx2 <= px <= tx1):
        if (ty1 <= py <= ty2) or (ty2 <= py <= ty1):
            print(tx1, px, tx2, ty1, py, ty2)
            return True
    return False


def getHigherValue(a, b):
    return a if abs(a) > abs(b) else b


def checkIfBeyondTarget(px, py):
    if px > getHigherValue(tx1, tx2):
        # if py < getHigherValue(ty1, ty2):
        print(tx1, px, tx2, ty1, py, ty2)
        return True
    if py < getHigherValue(ty1, ty2):
        # if px > getHigherValue(tx1, tx2):
        print(tx1, px, tx2, ty1, py, ty2)
        return True
    return False


def oneLoop(vx, vy, draw):
    done = False
    px = 0
    py = 0
    maxy = 0

    while done == False:
        px = px + vx
        py = py + vy
        print(px, py)
        if draw == True:
            plt.plot(px, py, 'o', color='blue')
        maxy = py if py > maxy else maxy

        target = checkIfTargetReached(px, py)
        if target == True:
            done = True
            print('Target area reached')
            print('maxY: ', maxy)

        beyond = checkIfBeyondTarget(px, py)
        if beyond == True:
            done = True
            print('Target missed')

        if vx != 0:
            if vx > 0:
                vx -= 1
            else:
                vx += 1
        vy -= 1

    return maxy, target, beyond


maxPair = [0, 0]
maxAbs = 0

for i in range(15):
    for j in range(15):
        print('------- ', i, j)
        maxy, target, beyond = oneLoop(i, j, False)
        if target and maxy > maxAbs:
            maxAbs = maxy
            maxPair = [i, j]

print('maximum height: ', maxAbs)

plt.axhline(y=0, linestyle='-', color='grey')
plt.axvline(x=0, linestyle='-', color='grey')
fig, ax = plt.subplots()
ax.add_patch(Rectangle((tx1, ty1), tx2-tx1, ty2-ty1))
ax.text(maxPair[0]+2, maxAbs-1, 'max: ' + str(maxAbs), fontsize=12)

oneLoop(maxPair[0], maxPair[1], True)

plt.grid()
plt.show()
