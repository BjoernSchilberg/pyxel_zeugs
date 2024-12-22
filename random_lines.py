# https://x.com/lawofcons/status/1868832505115426989
import random
import pyxel

width, height = 500, 100
borderx, bordery = 20, 10
y = 50
step = 10
lastx, lasty = -999, -999

pyxel.init(width, height, title="Drawing lines in Pyxel")
pyxel.cls(5)

for x in range(borderx, width - borderx, step):
    y = bordery + random.uniform(0, height - 2 * bordery)
    if lastx > -999:
        pyxel.line(x, y, lastx, lasty, 11)
    lastx = x
    lasty = y

pyxel.show()
