import pyxel

data = [40, 70, 50, 20, 100, 50, 40, 20]

pyxel.init(128, 128)

for i, d in enumerate(data):
    pyxel.rect(i * 14 + 10, 120 - d, 10, d, 8 + i)

pyxel.line(0, 120, 127, 120, 7)

pyxel.show()
