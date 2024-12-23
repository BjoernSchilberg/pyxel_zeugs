"""\
Boids is an artificial life program, which simulates the flocking behaviour of birds, and related group motion.

Some resources I'd recommend if you wanted to learn more about boids:
* https://en.wikipedia.org/wiki/Boids
* https://people.ece.cornell.edu/land/courses/ece4760/labs/s2021/Boids/Boids.html
* http://www.red3d.com/cwr/boids/

This is my quick excercise to make a simplified, 2d, retro inspiried implementation.
"""

import pyxel

NO_OF_BOIDS = 100
RESOLUTION = 256
VELOCITY = 1.2
TURNSPEED = 5
SIGHT = RESOLUTION / 10
AVOID = SIGHT / 2


def normalise(items: iter) -> tuple:
    high = max([abs(item) for item in items])
    if high:
        return tuple(item / high for item in items)
    else:
        return (0, 0)


class Boid:
    def __init__(self) -> None:
        self.x = pyxel.rndi(0, pyxel.width)
        self.y = pyxel.rndi(0, pyxel.height)
        self.direction = pyxel.rndi(-180, 180)

    def draw(self) -> None:
        pyxel.line(self.x, self.y, self.old_x, self.old_y,
                   pyxel.COLOR_DARK_BLUE)
        pyxel.pset(self.x, self.y, pyxel.COLOR_WHITE)

    def update(self, neighbours: "Boid" = None) -> None:

        if neighbours:
            # coherence/cohesion - steer towards center of mass

            n = len(neighbours)

            cx = sum(other.x for other in neighbours) / n - self.x
            cy = sum(other.y for other in neighbours) / n - self.y
            cx, cy = normalise((cx, cy))

            # avoidance/separation - steer away from close peers
            too_close = [
                (self.x - other.x, self.y - other.y)
                for other in neighbours
                if self.dist_sq(other) <= AVOID ** 2
            ]

            if len(too_close) > 0:
                dx, dy = normalise(tuple(map(sum, zip(*too_close))))
            else:
                dx, dy = 0, 0

            # alignment - matching direction
            sumsin = sum(pyxel.sin(other.direction) for other in neighbours)
            sumcos = sum(pyxel.cos(other.direction) for other in neighbours)
            ax, ay = normalise((sumcos, sumsin))

            ax -= dx * 0.5 + cx * 0.5
            ay -= dy * 0.5 + cy * 0.5

            if ax == 0 and ay < 0:
                avgdir = -180
            else:
                avgdir = pyxel.atan2(ay, ax)

            if avgdir > self.direction:
                self.direction += TURNSPEED
            else:
                self.direction -= TURNSPEED

        # border collision detection
        if self.x <= 0 or self.x >= pyxel.width:
            self.direction *= -1
        if self.y <= 0 or self.y >= pyxel.height:
            if self.direction >= 0:
                self.direction = 180 - self.direction
            else:
                self.direction = -180 - self.direction

        # calculate new position based on speed and direction
        self.old_x, self.old_y = self.x, self.y
        self.x = self.old_x + VELOCITY * pyxel.sin(self.direction)
        self.y = self.old_y - VELOCITY * pyxel.cos(self.direction)

    def dist_sq(self, other: "Boid"):
        return (self.x - other.x)**2 + (self.y - other.y)**2


class App:
    def __init__(self) -> None:
        pyxel.init(RESOLUTION, RESOLUTION, title="Boids", fps=60)
        self.boids = [Boid() for _ in range(NO_OF_BOIDS)]
        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        for boid in self.boids:
            pack = [
                other
                for other in self.boids
                if boid.dist_sq(other) <= SIGHT ** 2
            ]
            boid.update(pack)

    def draw(self) -> None:
        pyxel.cls(pyxel.COLOR_BLACK)

        for boid in self.boids:
            boid.draw()


App()
