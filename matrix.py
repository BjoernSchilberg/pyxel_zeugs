import random
import pyxel


class Matrix:
    def __init__(self):
        pyxel.init(160, 120)
        self.loop = 0

        self.width = pyxel.width // 4
        self.height = pyxel.height // 6

        self.shades = [
            {"color": pyxel.COLOR_WHITE, "len": 1},
            {"color": pyxel.COLOR_LIME, "len": self.height},
            {"color": pyxel.COLOR_GREEN, "len": 5},
            {"color": pyxel.COLOR_GRAY, "len": 3},
        ]
        self.strip_len = 0
        for shade in self.shades:
            self.strip_len += shade["len"]
            shade["cummulative_length"] = self.strip_len

        self.strips = [
            {
                "letters": [chr(random.randint(33, 128)) for i in range(self.height)],
                "pos": random.randint(-self.strip_len, 0),
            }
            for j in range(self.width)
        ]

        pyxel.run(self.update, self.draw)

    # only advance the animation on every n-th update
    speed = 3

    def update(self):
        if not self.loop % Matrix.speed:
            for stripe in self.strips:
                if stripe["pos"] > self.strip_len + self.height:
                    stripe["pos"] = random.randint(-self.strip_len, 0)
                else:
                    stripe["pos"] += 1

        # let's make 2 random letters glitch on every update
        for _ in range(2):
            buggy_strip = random.choice(self.strips)
            bug_pos = random.randint(0, len(buggy_strip["letters"]) - 1)
            buggy_strip["letters"][bug_pos] = chr(random.randint(33, 128))

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.loop += 1

    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)
        for x, strip in enumerate(self.strips):
            for y, letter in enumerate(strip["letters"]):
                step = strip["pos"] - y
                if 0 <= step < self.strip_len:
                    for shade in self.shades:
                        if step < shade["cummulative_length"]:
                            color = shade["color"]
                            break
                    pyxel.text(x * 4, y * 6, letter, color)


Matrix()
