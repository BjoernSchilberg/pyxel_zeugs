# https://note.com/pro_gramma/n/n3d83dc4525ca
import pyxel
from random import choice

SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200

PATTERN_SIZE = 13  # 模様のサイズ：奇数
SPACE_SIZE = 3  # 模様の感覚：奇数
DOT_SIZE = 6  # 一目のサイズ
COL_LIST = (1, 7)  # COL_LIST[0]：背景の色、COL_LIST[1]：模様の色


class Pattern:  # 模様のクラス
    def __init__(self):  # 模様のデータを0で初期化
        self.pattern_data = [
            [0 for _ in range(PATTERN_SIZE)] for _ in range(PATTERN_SIZE)
        ]
        self.x = 10  # 描画開始位置
        self.y = 10
        n = PATTERN_SIZE // 2  # 模様の外側の四角に1をセット
        for i in range(n + 1):
            j = n - i
            k = n + i
            self.pattern_data[i][j] = COL_LIST[1]
            self.pattern_data[i][k] = COL_LIST[1]
            self.pattern_data[PATTERN_SIZE - i - 1][j] = COL_LIST[1]
            self.pattern_data[PATTERN_SIZE - i - 1][k] = COL_LIST[1]

    def update(self):
        n = PATTERN_SIZE // 2  # 模様の内側はランダムに0か1をセット
        for i in range(1, n + 1):
            for j in range(i):
                k = choice([0, 1])
                self.pattern_data[i][n - j] = k  # 基本の模様
                self.pattern_data[n * 2 - i][n - j] = k  # 基本を上下に反転
                self.pattern_data[i][n + j] = k  # 基本を左右に反転
                self.pattern_data[n * 2 - i][n + j] = k  # 基本を上下左右に反転

    def draw(self):
        size = (
            PATTERN_SIZE + SPACE_SIZE
        ) * DOT_SIZE  # 模様を画面のサイズにあわせて描画
        for i in range(SCREEN_HEIGHT // size):
            y = size * i + self.y
            for j in range(SCREEN_WIDTH // size):
                x = size * j + self.x
                self.draw_pattern(x, y, DOT_SIZE, PATTERN_SIZE)
                if (x + size) < SCREEN_WIDTH and (y + size) < SCREEN_HEIGHT:
                    self.draw_pattern(
                        x + size / 2, y + size / 2, DOT_SIZE, PATTERN_SIZE
                    )

    def draw_pattern(self, x, y, w, n):  # 模様1つ分を描画
        x0 = x
        y0 = y
        for j in range(n):
            y = y0 + j * w
            for i in range(n):
                if self.pattern_data[j][i] != 0:
                    pyxel.rect(x0 + i * w, y, w, w, COL_LIST[1])


class App:
    def __init__(self):
        pyxel.init(
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            title="Sashiko Pattern",
            capture_scale=2,
            capture_sec=7,
        )
        self.pattern = Pattern()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.frame_count % 20 == 0:
            self.pattern.update()

    def draw(self):
        pyxel.cls(COL_LIST[0])
        self.pattern.draw()


App()
