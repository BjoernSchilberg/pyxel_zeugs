import pyxel
import random


w = 400
h = 400
pyxel.init(w, h)


def random_triangle():
    x1, y1 = random.randrange(w), random.randrange(h)
    x2, y2 = random.randrange(w), random.randrange(h)
    x3, y3 = random.randrange(w), random.randrange(h)
    color = pyxel.rndi(8, 12)
    pyxel.trib(x1, y1, x2, y2, x3, y3, color)


for _ in range(0, 100):
    random_triangle()

pyxel.show()
