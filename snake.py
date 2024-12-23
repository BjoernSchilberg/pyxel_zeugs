import pyxel, random
# https://www.pyxelstudio.net/hmn6ta4s

TITLE = "Snake"
WIDTH = 200
HEIGHT = 160
CASE = 20
FRAME_REFRESH = 15


class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, TITLE)
        self.snake = [[3, 3], [2, 3], [1, 3]]
        self.direction = [1, 0]
        self.score = 0
        self.food = [8, 3]

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.frame_count % FRAME_REFRESH == 0:
            head = [
                self.snake[0][0] + self.direction[0],
                self.snake[0][1] + self.direction[1],
            ]
            self.snake.insert(0, head)

            if (
                head in self.snake[1:]
                or head[0] < 0
                or head[0] > WIDTH / CASE - 1
                or head[1] < 0
                or head[1] > WIDTH / CASE - 1
            ):
                pyxel.quit()

            if head == self.food:
                self.score += 1
                while self.food in self.snake:
                    self.food = [
                        random.randint(0, int(WIDTH / CASE - 1)),
                        random.randint(0, int(HEIGHT / CASE - 1)),
                    ]
            else:  # On n'efface pas la queue > le serpent agrandit
                self.snake.pop()

        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.KEY_D):
            self.direction = [1, 0]
        elif pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.KEY_A):
            self.direction = [-1, 0]
        elif pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_W):
            self.direction = [0, -1]
        elif pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.KEY_S):
            self.direction = [0, 1]

    def draw(self):
        pyxel.cls(0)
        for anneau in self.snake[1:]:
            x, y = anneau[0], anneau[1]
            pyxel.rect(x * CASE, y * CASE, CASE, CASE, 11)
        x_head, y_head = self.snake[0]
        pyxel.rect(x_head * CASE, y_head * CASE, CASE, CASE, 9)

        x_food, y_food = self.food
        pyxel.rect(x_food * CASE, y_food * CASE, CASE, CASE, 8)

        pyxel.text(4, 4, f"SCORE : {self.score}", 7)


App()
