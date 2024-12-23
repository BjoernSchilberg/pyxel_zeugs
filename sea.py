"""
Draw a really simple animated picture of the sun with moving clouds on the top and blue
waves on the bottom with the Pyxel retro game engine.
"""

from math import sin
from time import monotonic
import pyxel

WIDTH = 160
HEIGHT = 120


def update():
    pass


def draw():
    pyxel.cls(pyxel.COLOR_WHITE)  # clear the canvas with white

    t = monotonic()

    # Draw the clouds with little dots.
    for y in range(HEIGHT // 10):
        for x in range(WIDTH // 5):
            s = sin((x * 0.1) + y + (t * 0.0125))
            if 0.5 < s < 0.7:
                pyxel.pset(x * 6, y * 4, pyxel.COLOR_LIGHT_BLUE)  # blue

    # Draw the sun with one circle and use another for hiding any clouds that may
    # appear too close to it.
    pyxel.circ(WIDTH / 2, 20, 15, 7)  # white
    pyxel.circ(WIDTH / 2, 20, 10, pyxel.COLOR_YELLOW)  # paint the sun with yellow

    # Draw the waves with tall narrow rectangles.
    for x in range(WIDTH):
        h = 20
        y = (HEIGHT - h) + sin((x * 0.1) + (t * 0.25)) * 3
        pyxel.rect(x, y, 1, h + 3, pyxel.COLOR_DARK_BLUE)  # blue


if __name__ == "__main__":
    pyxel.init(WIDTH, HEIGHT)
    pyxel.run(update, draw)
