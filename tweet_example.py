from pyxel import *
from math import *

a = 0
init(128, 128)
while 1:
    cls(1)
    for x in range(0, 128, 4):
        for y in range(0, 128, 4):
            d = sqrt((x - 64) ** 2 + (y - 64) ** 2)
            b = sin(d * 0.2 + a) * 4
            c = (15 - d * 0.2) % 16
            circ(x + b, y + sin(b / 4) * 4, 1, c)
    a += 0.2
    flip()
