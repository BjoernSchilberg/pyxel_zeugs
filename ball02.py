# https://tkitao.hatenablog.com/entry/2019/09/22/001541
import pyxel

x = y = 30  # the position of the ball
v = w = 3  # the speed of the ball

pyxel.init(160, 120)  # create the screen as 160x120 size

while True:
    pyxel.cls(1)  # erase the screen with color number 1 (blue)

    # process the movement of the ball
    x += v
    y += w

    if x <= 7 or x >= 152:
        x = min(max(x, 7), 152)
        v = -v

    if y <= 7 or y >= 112:
        y = min(max(y, 7), 112)
        w = -w

    pyxel.circ(x, y, 7, pyxel.frame_count % 16)  # draw the ball with different colors

    pyxel.flip()  # draw the screen
