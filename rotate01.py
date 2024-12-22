# https://note.com/pro_gramma/n/ned6a8d08d8c9
import pyxel

IMAGE_1 = [0, 0, 0, 15, 15, 0]  # image_bank, u, v, w, h, transparent_color


class App:
    def __init__(self):
        pyxel.init(110, 110, title="rotating square")
        image_bank = 0
        # イメージバンクに正方形を書き込む
        pyxel.images[image_bank].rectb(0, 0, 15, 15, 1)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(6)
        for y in range(10, 80, 20):
            for x in range(10, 80, 20):
                rotate = pyxel.frame_count // 6 * 5
                pyxel.blt(x, y, *IMAGE_1, rotate=rotate, scale=1)
                pyxel.blt(x + 10, y + 10, *IMAGE_1, rotate=rotate, scale=1)


App()
