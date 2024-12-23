import pyxel
# https://gist.github.com/kevsturman/4d226c268ffa7ebbb27c1382532643a4


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x, self.y = 0, 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width
        self.y = (self.y + 1) % pyxel.height

    def draw(self):
        pyxel.cls(0)
        for r in range(0, 160, 5):
            pyxel.circb(self.x, self.y, r, 9)
            pyxel.circb(160 - self.x, 120 - self.y, r, 9)


App()

