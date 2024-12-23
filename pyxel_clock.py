import pyxel
from datetime import datetime


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.i = ""
        pyxel.run(self.update, self.draw)

    def update(self):
        pyxel.cls(0)
        self.i = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    def draw(self):
        pyxel.text(10, 10, self.i, 6)


App()
