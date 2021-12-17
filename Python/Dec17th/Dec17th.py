from matplotlib import colors
from matplotlib.patches import Rectangle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

tx1 = 20
tx2 = 30
ty1 = -10
ty2 = -5

vx = 6
vy = 9

maxy = 0

px = 0
py = 0

done = False


def checkIfTargetReached():
    if (tx1 <= px <= tx2) or (tx2 <= px <= tx1):
        if (ty1 <= py <= ty2) or (ty2 <= py <= ty1):
            print(tx1, px, tx2, ty1, py, ty2)
            return True
    return False


def getHigherValue(a, b):
    return a if abs(a) > abs(b) else b


def checkIfBeyondTarget():
    if px > getHigherValue(tx1, tx2):
        #if py < getHigherValue(ty1, ty2):
            print(tx1, px, tx2, ty1, py, ty2)
            return True
    if py < getHigherValue(ty1, ty2):
        #if px > getHigherValue(tx1, tx2):
            print(tx1, px, tx2, ty1, py, ty2)
            return True
    return False


plt.axhline(y=0, linestyle='-', color='grey')
plt.axvline(x=0, linestyle='-', color='grey')
fig, ax = plt.subplots()
ax.add_patch(Rectangle((tx1, ty1), tx2-tx1, ty2-ty1))

while done == False:
    px = px + vx
    py = py + vy
    print(px, py)
    plt.plot(px, py, 'o')

    done = checkIfTargetReached()
    if done == True:
        print('Target area reached')

    beyond = checkIfBeyondTarget()
    if beyond == True:
        done = True
        print('Target missed')

    if vx != 0:
        if vx > 0:
            vx -= 1
        else:
            vx += 1
    vy -= 1

plt.grid()
plt.show()
