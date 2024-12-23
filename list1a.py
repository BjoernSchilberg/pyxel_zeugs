import pyxel
# ported from MSX Graphic workbook(1984) p.69 List 1a / MSXグラフィック・ワークブックからのPython移植

# https://gist.github.com/nogajun/981b2d7e597c4cd220a0eaaf40fdfd1e

size = 255
count = 36
step = size / count
color = pyxel.COLOR_WHITE

pyxel.init(size, size)
pyxel.cls(pyxel.COLOR_PURPLE)

for i in range(count):
    pyxel.line(step * i, size, size, size - step * i, color)
    pyxel.line(size - step * i, 0, size, size - step * i, color)
    pyxel.line(size - step * i, 0, 0, step * i, color)
    pyxel.line(step * i, size, 0, step * i, color)
    pyxel.flip()

pyxel.show()
