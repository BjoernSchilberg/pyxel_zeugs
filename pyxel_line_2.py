import pyxel
import math
# https://gist.github.com/MizunagiKB/e9e4f55a6edbd9c7fd81d67ae1ebf995
# 位置履歴を使ったレーザーの描画（２）


# レーザーの長さ
MAX_LASER_HISTORY = 8
# レーザー色（お好みで）
LASER_COLOR = [2, 2, 2, 2, 8, 9, 10, 7]
# レーザーの長さとレーザー色の数が一致しているかのチェック
# （数が誤っているとエラーを出して教えてくれます）
assert MAX_LASER_HISTORY == len(LASER_COLOR)


class CLaser(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.list_pos = []

    def move(self, x, y):
        self.x = x
        self.y = y
        # 昔の位置を保存
        self.list_pos.append((x, y))
        # 配列がMAX_LASER_HISTORY以下になる様に調整
        n = len(self.list_pos) - MAX_LASER_HISTORY
        if n > 0:
            self.list_pos = self.list_pos[n:]

    def draw_laser(self):
        # レーザーの描画
        for n, p in enumerate(self.list_pos[1:]):
            x_src, y_src = self.list_pos[n]
            x_dst, y_dst = p
            # ベクトルを計算
            vx, vy = x_dst - x_src, y_dst - y_src
            # 長さを計算（最低一回は描画するように補正）
            len = math.sqrt(vx * vx + vy * vy)
            if len < 1:
                len += 1
            # 絵をずらす単位を計算（単位ベクトル化）
            sx = vx / len
            sy = vy / len
            for _ in range(int(len)):
                # ずらしながら描画（ここでは単純に●を描画）
                pyxel.circ(x_src, y_src, 7, LASER_COLOR[n])
                x_src += sx
                y_src += sy

        pyxel.circ(self.x, self.y, 7, LASER_COLOR[-1])


def main():
    pyxel.init(256, 256)
    pyxel.mouse(True)

    # レーザーの初期化
    o_laser = CLaser(pyxel.mouse_x, pyxel.mouse_y)

    while True:
        pyxel.cls(5)
        # 敵弾の更新処理（ここではマウスの位置を設定）
        o_laser.move(pyxel.mouse_x, pyxel.mouse_y)
        # レーザーの描画
        o_laser.draw_laser()
        pyxel.flip()


if __name__ == "__main__":
    main()
