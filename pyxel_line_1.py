import pyxel

# https://gist.github.com/MizunagiKB/9cc0d9479d0f683485c39883dd78090f

# レーザーの長さ
MAX_LASER_HISTORY = 8
# レーザー色（お好みで）
LASER_COLOR = [7, 6, 5, 1, 1, 1, 1, 1]
# レーザーの長さとレーザー色の数が一致しているかのチェック
# （数が誤っているとエラーを出して教えてくれます）
assert MAX_LASER_HISTORY == len(LASER_COLOR)


class CLaser(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.list_pos = []

    def move(self, x, y):
        # 昔の位置を保存
        self.list_pos.insert(0, (self.x, self.y))
        # 新しい位置を記録
        self.x = x
        self.y = y
        # 配列がMAX_LASER_HISTORY以下になる様に調整
        self.list_pos = self.list_pos[0:MAX_LASER_HISTORY]

    def draw_laser(self):
        # レーザーの描画
        for n, p in enumerate(self.list_pos[1:]):
            x1, y1 = self.list_pos[n]
            x2, y2 = p
            pyxel.line(x1, y1, x2, y2, LASER_COLOR[n])


def main():
    pyxel.init(256, 256)
    pyxel.mouse(True)

    # レーザーの初期化
    o_laser = CLaser(pyxel.mouse_x, pyxel.mouse_y)

    while True:
        pyxel.cls(0)
        # 敵弾の更新処理（ここではマウスの位置を設定）
        o_laser.move(pyxel.mouse_x, pyxel.mouse_y)
        # レーザーの描画
        o_laser.draw_laser()
        pyxel.flip()


if __name__ == "__main__":
    main()
