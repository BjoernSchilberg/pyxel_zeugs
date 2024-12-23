import pyxel

pyxel.init(80, 64)
pyxel.load("my_resource.pyxres")

x = 0
y = 0
status = 0  # Add variables


def update():
    global x, y, status  # Add status
    x = pyxel.mouse_x
    y = pyxel.mouse_y
    if x == 5 and y == 5:  # Add coordinate judgment
        status = 1
    else:
        status = 0

    return


def draw():
    pyxel.cls(1)
    pyxel.blt(5, 5, 0, 8, 0, 8, 8, 11)  # Last argument Change transparent color
    pyxel.blt(x, y, 0, 8, 0, 8, 8, 0)

    if status == 1:  # Add a branch to display text
        pyxel.text(20, 7, "Hello world!", col=7, font=None)

    return


pyxel.run(update, draw)
