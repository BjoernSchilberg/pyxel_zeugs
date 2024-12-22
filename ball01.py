import pyxel

x = 0
pyxel.init(160, 120)

while True:
    x += 2
    if x >= pyxel.width + 20:
        x = -20

    pyxel.cls(0)
    pyxel.circ(x, 60, 20, 11)
    pyxel.flip()
