import math
import pyxel

# https://gist.github.com/BjoernSchilberg/8ff84ffe932c499043c08120c8b3a6ff
# https://web.archive.org/web/20190318014833/https://blog.vomkonstant.in/2019/01/21/pythons-most-underrated-game-engine-for-beginners/

BALL_SIZE = 2
BALL_SPEED = 2
BAT_SIZE = 8
SCREEN_WIDTH = 255
SCREEN_HEIGHT = 120


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vec2_norm:
    def __init__(self, x, y):
        self.magnitude = math.sqrt(x * x + y * y)
        self.x = x / self.magnitude * BALL_SPEED
        self.y = y / self.magnitude * BALL_SPEED


class HitBox:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1  # x-coordinate of top left corner
        self.y1 = y1  # y-coordinate of top left corner
        self.x2 = x2  # x-coordinate of bottom right corner
        self.y2 = y2  # y-coordinate of bottom right corner


class Ball:
    def __init__(self, px, py, vx, vy):
        self.position = Vec2(px, py)
        self.velocity = Vec2_norm(vx, vy)

    def update(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

        if self.position.y >= SCREEN_HEIGHT - BALL_SIZE:
            self.velocity.y = -self.velocity.y

        if self.position.y <= BALL_SIZE:
            self.velocity.y = -self.velocity.y


class Bat:
    def __init__(self, px, py):
        self.position = Vec2(px, py)
        self.velocity = 0
        self.hitBox = HitBox(
            self.position.x - BAT_SIZE / 4,
            self.position.y - BAT_SIZE,
            self.position.x + BAT_SIZE / 4,
            self.position.y + BAT_SIZE,
        )

    def update(self):
        self.position.y += self.velocity
        self.hitBox = HitBox(
            self.position.x - BAT_SIZE / 4,
            self.position.y - BAT_SIZE,
            self.position.x + BAT_SIZE / 4,
            self.position.y + BAT_SIZE,
        )

        if pyxel.btnp(pyxel.KEY_W):
            self.velocity = -2

        if pyxel.btnp(pyxel.KEY_S):
            self.velocity = 2

        if self.position.y - BAT_SIZE < 0:
            self.position.y = BAT_SIZE
            self.velocity = 0

        if self.position.y + BAT_SIZE > SCREEN_HEIGHT:
            self.position.y = SCREEN_HEIGHT - BAT_SIZE
            self.velocity = 0


class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.ball = Ball(20, 20, 2, 2)
        self.bats = [Bat(10, 10), Bat(SCREEN_WIDTH - 10, 10)]
        self.score = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.ball.update()
        for bat in self.bats:
            bat.update()
            if (
                bat.hitBox.x1 < self.ball.position.x < bat.hitBox.x2
                and bat.hitBox.y1 < self.ball.position.y < bat.hitBox.y2
            ):
                self.ball.velocity.x = -self.ball.velocity.x
                self.score += 1
        if self.ball.position.x >= SCREEN_WIDTH - BALL_SIZE:
            pyxel.quit()
        if self.ball.position.x <= BALL_SIZE:
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.circ(self.ball.position.x, self.ball.position.y, BALL_SIZE, 7)
        for bat in self.bats:
            pyxel.rect(bat.hitBox.x1, bat.hitBox.y1, bat.hitBox.x2, bat.hitBox.y2, 7)
        pyxel.text(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 12, str(self.score), 7)


App()
