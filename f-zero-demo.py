from random import randint
from math import sin, cos
import pyxel

# Made by AntoineTelgruc2 (yeah, that usename sucks)


class game:
    def __init__(self):
        self.level = [[randint(0, 15) for _ in range(32)] for _ in range(32)]
        self.dir = 0
        self.x = 35
        self.y = 34.14
        self.vel = 0
        self.velDir = 0
        pyxel.init(160, 100)
        pyxel.load("res.pyxres")
        # pyxel.image(0)
        # pyxel.tilemap(0)
        pyxel.run(self.controls, self.draw)

    def controls(self):
        self.vel += 0.01 * (pyxel.btn(pyxel.KEY_DOWN) - pyxel.btn(pyxel.KEY_UP))
        self.velDir += 0.015 * (pyxel.btn(pyxel.KEY_RIGHT) - pyxel.btn(pyxel.KEY_LEFT))
        self.vel *= 0.98
        self.velDir *= 0.85
        self.dir += self.velDir
        self.x += self.vel * sin(self.dir - 80.11061)
        self.y += self.vel * cos(self.dir - 80.11061)
        # 80.11061 is a magic number that somehow fixes a camera angle bug. I don't know what I messed up in the engine to get such a weird number but it works I guess...

    def draw(self):
        pyxel.cls(6)
        pyxel.rect(0, 0, 160, 10, 5)
        pyxel.rect(0, 10, 160, 15, 12)
        self.multiplier = 64
        for y in range(60):
            self.multiplier *= (100 - self.multiplier) / 100
            self.castX = (
                self.x
                + 4 * sin(self.dir - 80.11061)
                + 2.25 * (self.multiplier * sin(self.dir - 90))
            )
            self.castY = (
                self.y
                + 4 * cos(self.dir - 80.11061)
                + 2.25 * (self.multiplier * cos(self.dir - 90))
            )
            for x in range(160):
                pyxel.bltm(
                    x, y + 40, 0, int(self.castY * 30), int(self.castX * 30), 1, 1
                )
                self.castX += (self.multiplier / 80) * sin(self.dir)
                self.castY += (self.multiplier / 80) * cos(self.dir)
        pyxel.blt(64, 65, 0, 0, 32, 32, 32, 15)


game()
