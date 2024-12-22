# https://note.com/pro_gramma/n/ned6a8d08d8c9
import pyxel

IMAGE_1 = [0, 0, 0, 32, 32, 0]  # image_bank, u, v, w, h, transparent_color


class App:
    def __init__(self):
        pyxel.init(110, 110, title="rotating circle")
        image_bank, r, col = 0, 10, 1
        # イメージバンクに円を書き込む
        pyxel.images[image_bank].circb(0, 16, r, col)
        pyxel.images[image_bank].circb(32, 16, r, col)
        pyxel.images[image_bank].circb(16, 0, r, col)
        pyxel.images[image_bank].circb(16, 32, r, col)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(6)
        for y in range(0, 75, 32):
            for x in range(0, 75, 32):
                rotate = pyxel.frame_count // 6 * 5
                pyxel.blt(x, y, *IMAGE_1, rotate=rotate, scale=1)
                pyxel.blt(x + 16, y + 16, *IMAGE_1, rotate=rotate, scale=1)


App()
