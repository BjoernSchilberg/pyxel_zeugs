import pyxel
import math

# https://gist.github.com/miso24/3a6cb6a94d2a461c8eb09f80001ad38c


class Slider:
    ICON_WIDTH = 10

    def __init__(self, x, y, w, h, min_value, max_value, initial_value=None):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.min_value, self.max_value = min_value, max_value
        if initial_value is None or not min_value <= initial_value <= max_value:
            self.current_value = (min_value + max_value) // 2
        else:
            self.current_value = initial_value

    def update(self):
        if not pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            return
        mx, my = pyxel.mouse_x, pyxel.mouse_y
        if not self.x < mx <= self.x + self.w or not self.y < my < self.y + self.h:
            return
        self.current_value = (
            int(((mx - self.x) / self.w) * (self.max_value - self.min_value))
            + self.min_value
        )

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, 1)
        dx = (
            self.x
            + (
                (self.current_value - self.min_value)
                / (self.max_value - self.min_value)
            )
            * self.w
            - Slider.ICON_WIDTH // 2
        )
        pyxel.rect(dx, self.y, Slider.ICON_WIDTH, self.h, 7)

    @property
    def value(self):
        return self.current_value


def tree(x, y, depth, theta, length, scale, col, base_theta=90):
    if not depth or length < 1:
        return
    r = math.radians(base_theta)
    x2 = x + math.cos(r) * length
    y2 = y - math.sin(r) * length
    pyxel.line(x, y, x2, y2, col)
    tree(x2, y2, depth - 1, theta, length * scale, scale, col, base_theta + theta)
    tree(x2, y2, depth - 1, theta, length * scale, scale, col, base_theta - theta)


def main():
    pyxel.init(256, 256)
    pyxel.mouse(True)
    x, y = pyxel.width // 2, pyxel.height - 20
    depth = Slider(8, 14, 100, 8, 0, 10)
    theta = Slider(8, 28, 100, 8, 0, 180)
    length = Slider(8, 42, 100, 8, 10, 60)
    scale = Slider(8, 56, 100, 8, 0, 100)
    col = Slider(132, 14, 100, 8, 1, 15, 4)
    while True:
        pyxel.cls(0)
        tree(x, y, depth.value, theta.value, length.value, scale.value / 100, col.value)
        pyxel.text(8, 8, f"Depth : {depth.value}", 7)
        pyxel.text(8, 22, f"Theta : {theta.value}", 7)
        pyxel.text(8, 36, f"Length: {length.value}", 7)
        pyxel.text(8, 50, f"Scale : {scale.value / 100}", 7)
        pyxel.text(132, 8, f"Color: {col.value}", 7)
        for slider in [depth, theta, length, scale, col]:
            slider.update()
            slider.draw()
        pyxel.flip()


if __name__ == "__main__":
    main()
