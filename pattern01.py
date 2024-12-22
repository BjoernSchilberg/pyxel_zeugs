# https://note.com/pro_gramma/n/ne8c470703996
import pyxel
from random import choice

SCREEN_WIDTH = 180
SCREEN_HEIGHT = 180

PATTERN_SIZE = 13  # 模様のサイズ：奇数
SPACE_SIZE = 1  # 模様の間隔
DOT_SIZE = 4  # 一目のサイズ
BACKGROUND_COLOR = 1  # 背景の色
COL_LIST = [1, 12, 7]  # 模様の色


class Pattern:  # 模様のクラス
    def __init__(self):
        n = PATTERN_SIZE + 1  # 模様のデータを初期化
        self.pattern_data = [[BACKGROUND_COLOR for _ in range(n)] for _ in range(n)]
        self.x = 10  # 描画開始位置
        self.y = 10

    def update(self):
        n = PATTERN_SIZE // 2
        for i in range(n + 1):  # 基本の模様
            for j in range(i, n + 1):
                k = choice(COL_LIST)
                self.pattern_data[i][j] = k
                if j > i:
                    self.pattern_data[j][i] = k

        for i in range(n + 1):
            for j in range(n + 1):
                k = self.pattern_data[i][j]
                self.pattern_data[n * 2 - i][j] = k  # 基本を左右に反転
                self.pattern_data[i][n * 2 - j] = k  # 基本を上下に反転
                self.pattern_data[n * 2 - i][n * 2 - j] = k  # 基本を上下左右に反転

    def draw(self):
        size = (
            PATTERN_SIZE + SPACE_SIZE
        ) * DOT_SIZE  # 模様を画面のサイズにあわせて描画
        for i in range(SCREEN_HEIGHT // size):
            y = size * i + self.y
            for j in range(SCREEN_WIDTH // size):
                x = size * j + self.x
                self.draw_pattern(x, y, DOT_SIZE, PATTERN_SIZE)

    def draw_pattern(self, x, y, w, n):  # 模様1つ分を描画
        x0 = x
        y0 = y
        for j in range(n + 1):
            y = y0 + j * w
            for i in range(n + 1):
                pyxel.rect(x0 + i * w, y, w, w, self.pattern_data[i][j])


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
        pyxel.cls(BACKGROUND_COLOR)
        self.pattern.draw()


App()
