import pyxel
# https://kinutani.hateblo.jp/entry/2023/04/23/221816

pyxel.init(128, 128)

player_x = 0
player_y = 0
enemy_x = 64
enemy_y = 64
deg = 0


def update():
    global player_x, player_y, deg
    player_x = pyxel.mouse_x
    player_y = pyxel.mouse_y
    x = player_x - enemy_x
    y = player_y - enemy_y
    deg = pyxel.atan2(y, x)
    return


def draw():
    pyxel.cls(0)
    pyxel.text(player_x, player_y, "P", col=7, font=None)

    r = 16
    pyxel.circb(enemy_x, enemy_y, r, 10)
    x = pyxel.cos(deg) * r
    y = pyxel.sin(deg) * r
    pyxel.circ(x + enemy_x, y + enemy_y, 2, 3)

    pyxel.text(1, 1, str(deg), col=7, font=None)
    return


pyxel.run(update, draw)
