# https://note.com/pro_gramma/n/n3f1b51a25f60
# Peter de Jong Attractor
# https://paulbourke.net/fractals/peterdejong/
from pyxel import *
from math import sin, cos
from random import choice, uniform

w = 256  # screen size
background_color = 0
dot_color = [3, 6, 9, 10, 14]
dot_count = 20000
p_min, p_max = -3, 3
init(w, w, fps=1)


def draw():
    cls(background_color)
    col = choice(dot_color)
    x, y = 0, 0
    a, b, c, d = [round(uniform(p_min, p_max), 2) for _ in range(4)]
    text(10, 10, "a=" + str(a) + " b=" + str(b) + " c=" + str(c) + " d=" + str(d), 7)
    for _ in range(dot_count):
        x, y = sin(a * y) - cos(b * x), sin(c * x) - cos(d * y)
        pset(x * w / 5 + 128, y * w / 5 + 140, col)


def update():
    pass


run(update, draw)
