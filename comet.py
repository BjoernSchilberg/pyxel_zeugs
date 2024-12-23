# https://gist.github.com/JohnEdChristensen/10edb85332fa4d7f6a035373c631268c
import dataclasses
import pyxel
import numpy as np

WIDTH = 210
HEIGHT = 150
SHIP_SIZE = 7
PLAYER_COLOR = 1
ENEMY_COLOR = 4
PLAYER_SPEED = 0.1
PLAYER_ROT_SPEED = np.pi / 16

BACKGROUND_COLOR = 0


def rotate_point(x: float, y: float, angle_rad: float) -> tuple[float, float]:
    """rotate point (x,y) about origin by angle_rad"""
    xRotated = x * np.cos(angle_rad) - y * np.sin(angle_rad)
    yRotated = x * np.sin(angle_rad) + y * np.cos(angle_rad)
    return xRotated, yRotated


def rotate_about_point(
    x: float, y: float, aboutX: float, aboutY: float, angle_rad: float
) -> tuple[float, float]:
    """rotate point (x,y) about point (aboutX,aboutY) by angle_rad"""
    # treat aboutX,aboutY as origin
    xRelative = aboutX - x
    yRelative = aboutY - y
    # apply rotation about origin
    xRelativeRotated, yRelativeRotated = rotate_point(xRelative, yRelative, angle_rad)
    # convert back to original coordinate space and return
    return xRelativeRotated + aboutX, yRelativeRotated + aboutY


@dataclasses.dataclass
class Ship:
    x: float
    y: float
    ship_color: int
    vx: float = 0
    vy: float = 0
    direction_rad: float = 0

    def draw_ship(self):
        # treat ship origin as x,y
        # get remaining points by rotating about x,y

        # ship is an isosceles triangle, pointing to the right >
        p2x = self.x - SHIP_SIZE
        p2y = self.y - SHIP_SIZE // 2
        p3x = self.x - SHIP_SIZE
        p3y = self.y + SHIP_SIZE // 2

        rotated_p2x, rotated_p2y = rotate_about_point(
            p2x, p2y, self.x, self.y, self.direction_rad
        )
        rotated_p3x, rotated_p3y = rotate_about_point(
            p3x, p3y, self.x, self.y, self.direction_rad
        )

        pyxel.tri(
            self.x,
            self.y,
            rotated_p2x,
            rotated_p2y,
            rotated_p3x,
            rotated_p3y,
            self.ship_color,
        )

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.x %= WIDTH
        self.y %= HEIGHT


player = Ship(WIDTH // 2, HEIGHT // 2, PLAYER_COLOR)
enemy = Ship(WIDTH // 4, HEIGHT // 4, ENEMY_COLOR, 0.5, -0.6)  # start adrift


class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Comets")
        # make sure to run this after initializing variables!
        pyxel.run(self.update, self.draw)

    def update(self):
        # inputs
        if pyxel.btn(pyxel.KEY_W):
            player.vy += -1 * PLAYER_SPEED * np.sin(player.direction_rad)
            player.vx += -1 * PLAYER_SPEED * np.cos(player.direction_rad)
        if pyxel.btn(pyxel.KEY_A):
            player.direction_rad -= PLAYER_ROT_SPEED
            print(f"{player.direction_rad/np.pi} pi rads")
        if pyxel.btn(pyxel.KEY_D):
            player.direction_rad += PLAYER_ROT_SPEED
            print(f"{player.direction_rad/np.pi} pi rads")

        enemy.update()
        player.update()

    def draw(self):
        pyxel.cls(BACKGROUND_COLOR)

        player.draw_ship()
        enemy.draw_ship()


App()
