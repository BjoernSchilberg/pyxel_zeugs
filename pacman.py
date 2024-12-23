import pyxel
import random


class Button:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.lx = x
        self.ly = y
        self.ix = x
        self.iy = y
        self.mix = x
        self.miy = y
        self.r = r
        self.a = True

    def update(self):
        mx, my = pyxel.mouse_x, pyxel.mouse_y
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            if self.a:
                self.a = False
                self.mix, self.miy = mx, my
            else:
                dist = int(
                    self.dist(
                        self.ix + (self.mix - self.ix),
                        self.iy + (self.miy - self.iy),
                        self.mix,
                        my,
                    )
                )
                if dist < 35:
                    self.y = self.iy - (self.miy - my)

                dist = int(
                    self.dist(
                        self.ix + (self.mix - self.ix),
                        self.iy + (self.miy - self.iy),
                        mx,
                        self.miy,
                    )
                )
                if dist < 35:
                    self.x = self.ix - (self.mix - mx)
        else:
            self.x = self.ix
            self.y = self.iy
            self.a = True

    def draw(self):
        pyxel.circb(self.ix, self.iy, self.r - 1, 7)
        pyxel.circ(self.x, self.y, self.r, 1)
        pyxel.circ(self.x, self.y, self.r - 10, 7)
        pyxel.circ(self.x - 2, self.y - 2, self.r - 10, 1)

    def dist(self, x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


class Monstre:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.px = x
        self.py = y
        self.type = type
        self.phase = 0
        self.pos = []
        self.d = "u"
        self.start = 0
        self.path = []
        self.c = False
        self.p = ["u", "r", "d", "l"]

    def update(self, perso):
        if not perso.phase:
            self.c = False
        if self.phase == -1:
            if self.path == []:
                self.phase = 0
                self.x = self.px
                self.y = self.py
            else:
                x, y = self.path[0][0], self.path[0][1]
                self.x = x * 8
                self.y = y * 8
                self.path.pop(0)

        if self.phase == 0:
            self.c = False
            if pyxel.frame_count - self.start > 60:
                if self.x == w // 2:
                    self.phase = 1
                elif self.x < w // 2:
                    self.x += 1
                elif self.x > w // 2:
                    self.x -= 1
        if self.phase == 1:
            if self.y == 92:
                self.phase = 2
            else:
                self.y -= 1
        if self.phase == 2:
            prev = self.pos
            self.pos = []
            if (
                pyxel.tilemap(0).pget((self.x - mres) // 8, (self.y - mres - 1) // 8)
                not in mur
                and pyxel.tilemap(0).pget(
                    (self.x + mres - 1) // 8, (self.y - mres - 1) // 8
                )
                not in mur
            ):
                self.pos.append("u")
            if (
                pyxel.tilemap(0).pget((self.x - mres) // 8, (self.y + mres) // 8)
                not in mur
                and pyxel.tilemap(0).pget(
                    (self.x + mres - 1) // 8, (self.y + mres) // 8
                )
                not in mur
            ):
                self.pos.append("d")
            if (
                pyxel.tilemap(0).pget((self.x + mres) // 8, (self.y - mres) // 8)
                not in mur
                and pyxel.tilemap(0).pget(
                    (self.x + mres) // 8, (self.y + mres - 1) // 8
                )
                not in mur
            ):
                self.pos.append("r")
            if (
                pyxel.tilemap(0).pget((self.x - mres - 1) // 8, (self.y - mres) // 8)
                not in mur
                and pyxel.tilemap(0).pget(
                    (self.x - mres - 1) // 8, (self.y + mres - 1) // 8
                )
                not in mur
            ):
                self.pos.append("l")
            if self.p[(self.p.index(self.d) + 2) % 4] in self.pos:
                self.pos.remove(self.p[(self.p.index(self.d) + 2) % 4])
            if prev != self.pos and pyxel.frame_count - self.start > 10:
                self.start = pyxel.frame_count
                self.d = random.choice(self.pos)

            if self.d == "u":
                if (
                    pyxel.tilemap(0).pget(
                        (self.x - mres + 1) // 8, (self.y - mres - 1) // 8
                    )
                    not in mur
                    and pyxel.tilemap(0).pget(
                        (self.x + mres - 1) // 8, (self.y - mres - 1) // 8
                    )
                    not in mur
                ):
                    self.y -= 1
            if self.d == "d":
                if (
                    pyxel.tilemap(0).pget((self.x - mres) // 8, (self.y + mres) // 8)
                    not in mur
                    and pyxel.tilemap(0).pget(
                        (self.x + mres - 1) // 8, (self.y + mres) // 8
                    )
                    not in mur
                ):
                    self.y += 1
            if self.d == "l":
                if (
                    pyxel.tilemap(0).pget(
                        (self.x - mres - 1) // 8, (self.y - mres + 1) // 8
                    )
                    not in mur
                    and pyxel.tilemap(0).pget(
                        (self.x - mres - 1) // 8, (self.y + mres - 1) // 8
                    )
                    not in mur
                ):
                    self.x -= 1
            if self.d == "r":
                if (
                    pyxel.tilemap(0).pget(
                        (self.x + mres) // 8, (self.y - mres + 1) // 8
                    )
                    not in mur
                    and pyxel.tilemap(0).pget(
                        (self.x + mres) // 8, (self.y + mres - 1) // 8
                    )
                    not in mur
                ):
                    self.x += 1
        if self.x > w - mres:
            self.x = mres + 1
        elif self.x < mres + 1:
            self.x = w - mres

    def draw(self):
        if self.c:
            pyxel.blt(self.x - mres, self.y - mres, 1, 32, 0, res, res, 11)
        else:
            if self.type == 1:
                pyxel.blt(self.x - mres, self.y - mres, 1, 16, 0, res, res, 11)
            if self.type == 2:
                pyxel.blt(self.x - mres, self.y - mres, 1, 24, 0, res, res, 11)
            if self.type == 3:
                pyxel.blt(self.x - mres, self.y - mres, 1, 16, 8, res, res, 11)
            if self.type == 4:
                pyxel.blt(self.x - mres, self.y - mres, 1, 24, 8, res, res, 11)


class Perso:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 3
        self.an = True
        self.sens = 1
        self.d = "r"
        self.dir = [
            (res, res, 0, res),
            (res, res, 0, 0),
            (res, -res, 0, res),
            (-res, res, 0, 0),
        ]
        self.phase = False
        self.start = 0

    def update(self, B):
        if pyxel.frame_count % 10 == 0:
            self.an = not self.an
        mx = pyxel.mouse_x
        my = pyxel.mouse_y

        """
            pyxel.blt(w//2+res+1,h+res*3,0,16,16,16,16)
            pyxel.blt(w//2-res,h+res-1,0,16*2,16,16,16)
            pyxel.blt(w//2-res,h+res*5+1,0,16*3,16,16,16)
            pyxel.blt(w//2-res*3-1,h+res*3,0,16*4,16,16,16)
        """

        if (
            (pyxel.btn(pyxel.KEY_UP) or (B.y < B.iy - (B.r // 2 - 5)))
            and pyxel.tilemap(0).pget((self.x - mres) // 8, (self.y - mres - 1) // 8)
            not in mur
            and pyxel.tilemap(0).pget(
                (self.x + mres - 1) // 8, (self.y - mres - 1) // 8
            )
            not in mur
        ):
            self.d = "u"
        if (
            (pyxel.btn(pyxel.KEY_DOWN) or (B.y > B.iy + (B.r // 2 - 5)))
            and pyxel.tilemap(0).pget((self.x - mres) // 8, (self.y + mres) // 8)
            not in mur
            and pyxel.tilemap(0).pget((self.x + mres - 1) // 8, (self.y + mres) // 8)
            not in mur
        ):
            self.d = "d"
        if (
            (pyxel.btn(pyxel.KEY_RIGHT) or (B.x > B.ix + (B.r // 2 - 5)))
            and pyxel.tilemap(0).pget((self.x + mres) // 8, (self.y - mres) // 8)
            not in mur
            and pyxel.tilemap(0).pget((self.x + mres) // 8, (self.y + mres - 1) // 8)
            not in mur
        ):
            self.d = "r"
        if (
            (pyxel.btn(pyxel.KEY_LEFT) or (B.x < B.ix - (B.r // 2 - 5)))
            and pyxel.tilemap(0).pget((self.x - mres - 1) // 8, (self.y - mres) // 8)
            not in mur
            and pyxel.tilemap(0).pget(
                (self.x - mres - 1) // 8, (self.y + mres - 1) // 8
            )
            not in mur
        ):
            self.d = "l"

        if (
            self.d == "u"
            and pyxel.tilemap(0).pget(
                (self.x - mres + 1) // 8, (self.y - mres - 1) // 8
            )
            not in mur
            and pyxel.tilemap(0).pget(
                (self.x + mres - 1) // 8, (self.y - mres - 1) // 8
            )
            not in mur
        ):
            self.y -= 1
            self.sens = 0
        if (
            self.d == "d"
            and pyxel.tilemap(0).pget((self.x - mres) // 8, (self.y + mres) // 8)
            not in mur
            and pyxel.tilemap(0).pget((self.x + mres - 1) // 8, (self.y + mres) // 8)
            not in mur
        ):
            self.y += 1
            self.sens = 2
        if (
            self.d == "l"
            and pyxel.tilemap(0).pget(
                (self.x - mres - 1) // 8, (self.y - mres + 1) // 8
            )
            not in mur
            and pyxel.tilemap(0).pget(
                (self.x - mres - 1) // 8, (self.y + mres - 1) // 8
            )
            not in mur
        ):
            self.x -= 1
            self.sens = 3
        if (
            self.d == "r"
            and pyxel.tilemap(0).pget((self.x + mres) // 8, (self.y - mres + 1) // 8)
            not in mur
            and pyxel.tilemap(0).pget((self.x + mres) // 8, (self.y + mres - 1) // 8)
            not in mur
        ):
            self.x += 1
            self.sens = 1

        if self.x > w - mres:
            self.x = mres + 1
        elif self.x < mres + 1:
            self.x = w - mres

    def draw(self):
        if self.an:
            W, H, X, Y = self.dir[self.sens]
            pyxel.blt(self.x - mres, self.y - mres, 1, X, Y, W, H, 8)
        else:
            pyxel.blt(self.x - mres, self.y - mres, 1, res, 0, res, res, 8)


class Jeu:
    def __init__(self):
        global w, h, mres, res, mur, map, M
        mur = [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (4, 0),
            (5, 0),
            (6, 0),
            (7, 0),
            (8, 0),
            (9, 0),
            (10, 0),
            (11, 0),
            (12, 0),
            (13, 0),
            (14, 0),
            (15, 0),
            (0, 1),
            (1, 1),
            (2, 1),
            (3, 1),
            (4, 1),
            (5, 1),
            (6, 1),
            (7, 1),
            (8, 1),
            (9, 1),
            (10, 1),
            (11, 1),
            (12, 1),
            (13, 1),
            (14, 1),
        ]
        M = [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (4, 0),
            (5, 0),
            (6, 0),
            (7, 0),
            (8, 0),
            (9, 0),
            (10, 0),
            (11, 0),
            (12, 0),
            (13, 0),
            (14, 0),
            (0, 1),
            (1, 1),
            (2, 1),
            (3, 1),
            (4, 1),
            (5, 1),
            (6, 1),
            (7, 1),
            (8, 1),
            (9, 1),
            (10, 1),
            (11, 1),
            (12, 1),
            (13, 1),
            (14, 1),
        ]
        res = 8
        mres = res // 2
        w = res * 28
        h = res * 31
        self.msg = []
        map = [[0 for _ in range(w // 8)] for _ in range(h // 8)]
        pyxel.init(w, h + 150, display_scale=2)
        pyxel.load("pac.pyxres")
        pyxel.mouse(False)
        self.perso = Perso(res * 14, res * 23 + mres)
        self.score = 0
        self.pg = 246
        self.edit = True
        self.start = 0
        m1 = Monstre(95, 122, 1)
        m2 = Monstre(95, 110, 2)
        m3 = Monstre(130, 122, 3)
        m4 = Monstre(130, 110, 4)
        self.monstre = [m1, m2, m3, m4]
        self.B = Button(w // 2, h + (150 // 2), 40)
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.edit:
            self.edit = False
            for i in range(h // 8):
                for k in range(w // 8):
                    if pyxel.tilemap(0).pget(k, i) in M:
                        map[i][k] = 1
            for i in map:
                print(i)
        if self.pg != 0 and self.perso.hp != 0:
            self.B.update()
            self.perso.update(self.B)
            if self.perso.phase:
                if pyxel.frame_count - self.perso.start > 300:
                    self.perso.phase = False
            for m in self.monstre:
                m.update(self.perso)
                if (
                    self.perso.x - mres < m.x < self.perso.x + mres
                    and self.perso.y - mres < m.y < self.perso.y + mres
                ):
                    if m.c:
                        self.score += 10
                        self.msg = [m.x, m.y]
                        self.start = pyxel.frame_count
                        m.path = find_path(
                            map, (m.x // 8, m.y // 8), (m.px // 8, m.py // 8)
                        )
                        print(m.x, m.y)
                        print(m.px, m.py)
                        print(m.path)
                        MM = [k for k in map]
                        for i in m.path:
                            x, y = i
                            print(x, y, map[x][y])
                            MM[y][x] = 2
                        for r in MM:
                            s = ""
                            for l in r:
                                if l == 0:
                                    s += " "
                                if l == 1:
                                    s += "#"
                                if l == 2:
                                    s += "x"
                            print(s)

                        m.x = m.px
                        m.y = m.py
                        m.phase = -1
                        m.start = pyxel.frame_count
                    else:
                        self.perso.hp -= 1
                        self.perso.x = res * 14
                        self.perso.y = res * 23 + mres
                        self.perso.d = "u"
            if pyxel.tilemap(0).pget(self.perso.x // 8, self.perso.y // 8) == (15, 1):
                self.score += 1
                self.pg -= 1
                pyxel.tilemap(0).pset(self.perso.x // 8, self.perso.y // 8, (0, 2))
            elif pyxel.tilemap(0).pget(self.perso.x // 8, self.perso.y // 8) == (16, 0):
                self.score += 10
                self.pg -= 1
                self.perso.phase = True
                self.perso.start = pyxel.frame_count
                for m in self.monstre:
                    m.c = True
                pyxel.tilemap(0).pset(self.perso.x // 8, self.perso.y // 8, (0, 2))

    def draw(self):
        pyxel.cls(0)
        if self.pg != 0 and self.perso.hp != 0:
            pyxel.bltm(0, 0, 0, 0, 0, w, h)
            self.perso.draw()
            self.B.draw()
            if self.msg != []:
                if pyxel.frame_count - self.start > 15:
                    self.msg = []
                else:
                    x, y = self.msg
                    pyxel.text(x - mres, y - mres, "+10p", 7)
            for m in self.monstre:
                m.draw()
            pyxel.text(1, 81, "score :" + str(self.score), 7)
            for i in range(self.perso.hp):
                pyxel.blt(188 + (10 * i), 85, 1, 0, 0, res, res, 8)
        elif self.pg == 0:
            pyxel.text(1, 1, "WIN", 7)
        else:
            pyxel.text(1, 1, "GAME OVER", 7)


Jeu()

