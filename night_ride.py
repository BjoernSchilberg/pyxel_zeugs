"""
Draw a really simple animated picture of a night sky with the moon and moving clouds on
the top, moving trees on the bottom and a moving lamp post with the Pyxel retro game
engine.
https://gist.github.com/catsocks/5040211552fd13ded7e9a6a26fc04913
"""

import math
import time
import pyxel

WIDTH = 160
HEIGHT = 120


def update():
    pass


def draw():
    pyxel.cls(1)  # paint the canvas dark blue

    t = time.monotonic()

    # Draw the clouds.
    for y in range(HEIGHT // 10):
        for x in range(WIDTH // 5):
            s = math.sin((x * 0.1) + y + (t * 0.0125))
            if s < -0.9:
                pyxel.pset(x * 6, y * 4, 13)  # grey
            elif s > 0.5 and s < 0.7:
                pyxel.pset(x * 6, y * 4, 7)  # white

    # Paint the moon with one circle and use another for hiding any stars that may
    # appear too close to it.
    pyxel.circ(WIDTH - 20, 20, 20, 1)  # dark blue
    pyxel.circ(WIDTH - 20, 20, 10, 7)  # paint the moon with white

    # Draw trees using circles.
    for x in range(5):
        h = (HEIGHT / 4) + math.sin(x + t) * 10
        pyxel.circ(x * (WIDTH / 4), HEIGHT, h, 3)  # green

    # Draw a lamp post with two narrow tall rectangles.
    pyxel.rect(WIDTH - (t * 120) % (WIDTH * 2), 0, 2, HEIGHT, 5)  # blue
    pyxel.rect(WIDTH - (t * 120) % (WIDTH * 2) + 2, 0, 3, HEIGHT, 12)  # light blue


if __name__ == "__main__":
    pyxel.init(WIDTH, HEIGHT)
    pyxel.run(update, draw)
