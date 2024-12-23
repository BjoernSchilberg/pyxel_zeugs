#!/usr/bin/env python3
# https://gist.github.com/greg76/f3b7e8f8d46a9bc1cafa60fdb61ae2e6
import math

import pyxel


class Intro:
    def __init__(self):
        pyxel.init(160, 120)
        self.xm = pyxel.width // 2
        self.max_width = pyxel.height // 2

        # how many times a light streak is circulating the tree
        self.rounds = 2
        self.t = 0
        self.rot_speed = 0.175

        # high & low intensity colors of the different light streaks
        self.color_shades = ((7, 13), (12, 1), (8, 2), (9, 4))

        # light streaks are "bleeding" into the background
        # not changing to a darker shade right at the edge
        self.roll_over = -0.4

        # not letting the "lights" form a solid line at the top
        # won't draw a light for every row and the distribution should be non-linear
        layers = 100
        self.y_slots = [
            pyxel.height - ((layers - y) / layers) ** 1.5 * pyxel.height
            for y in range(layers)
        ]

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        for y in self.y_slots:
            a = y / pyxel.height * self.max_width

            for i, (hi, lo) in enumerate(self.color_shades):
                phase_delta = math.pi * 2 * i / (len(self.color_shades) + 1)
                rad = (
                    y + self.t
                ) / pyxel.height * math.pi * 2 * self.rounds + phase_delta
                x = self.xm + a * math.sin(rad)

                z = math.cos(rad)
                color = hi if z > self.roll_over else lo

                pyxel.pset(x, y, color)

        self.t += self.rot_speed


Intro()
