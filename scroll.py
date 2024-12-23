import math
import random

import pyxel


class Intro:
    def __init__(self):
        pyxel.init(160, 120)
        self.amplitude = 10
        self.spacing = 4
        self.title = "Twin Sector Inc. is back! Greg sends his greetings to his old pals: TSC & Genesis!"
        self.xs = (pyxel.width - len(self.title) * self.spacing) / 2
        self.xs = pyxel.width
        self.starfield = [
            [
                random.randint(0, pyxel.width),
                random.randint(0, pyxel.height),
                random.randint(0, 2),
            ]
            for _ in range(100)
        ]
        self.star_shades = (7, 13, 1)

        pyxel.sounds[0].set(
            "e2e2c2g1 g1g1c2e2 d2d2d2g2 g2g2rr" "c2c2a1e1 e1e1a1c2 b1b1b1e2 e2e2rr",
            "p",
            "6",
            "vffn fnff vffs vfnn",
            25,
        )

        pyxel.sounds[1].set(
            "r a1b1c2 b1b1c2d2 g2g2g2g2 c2c2d2e2" "f2f2f2e2 f2e2d2c2 d2d2d2d2 g2g2r r ",
            "s",
            "6",
            "nnff vfff vvvv vfff svff vfff vvvv svnn",
            25,
        )

        pyxel.sounds[2].set(
            "c1g1c1g1 c1g1c1g1 b0g1b0g1 b0g1b0g1" "a0e1a0e1 a0e1a0e1 g0d1g0d1 g0d1g0d1",
            "t",
            "7",
            "n",
            25,
        )

        pyxel.sounds[3].set(
            "f0c1f0c1 g0d1g0d1 c1g1c1g1 a0e1a0e1" "f0c1f0c1 f0c1f0c1 g0d1g0d1 g0d1g0d1",
            "t",
            "7",
            "n",
            25,
        )

        pyxel.sounds[4].set(
            "f0ra4r f0ra4r f0ra4r f0f0a4r", "n", "6622 6622 6622 6422", "f", 25
        )

        pyxel.play(0, [0, 1], loop=True)
        pyxel.play(1, [2, 3], loop=True)
        pyxel.play(2, 4, loop=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        for i, star in enumerate(self.starfield):
            pyxel.pset(star[0], star[1], self.star_shades[star[2]])
            if star[0] > pyxel.width:
                self.starfield[i] = [
                    0,
                    random.randint(0, pyxel.height),
                    random.randint(0, len(self.star_shades) - 1),
                ]
            elif not pyxel.frame_count % (star[2] + 1):
                self.starfield[i][0] += 1

        for i, letter in enumerate(self.title):
            x = self.xs + i * self.spacing
            rot = (pyxel.frame_count - i * 2) / 10
            y = pyxel.height / 2 + self.amplitude * math.sin(rot)
            color = (pyxel.frame_count + i) % 16
            pyxel.text(x, y, letter, color)

        if self.xs < -len(self.title) * self.spacing:
            self.xs = pyxel.width
        else:
            self.xs -= 1


Intro()
