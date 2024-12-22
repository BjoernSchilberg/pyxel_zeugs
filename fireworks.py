# https://x.com/pro_gramma/status/1812733416598913100
# https://note.com/pro_gramma/n/n7ad87e89af41
import pyxel

EXPLOSION_SOUND = ("b3c3g2g2", "n", "4322", "f", 10)  # 花火が開く音
SHOOT_SOUND = ("rrrre3a3a3", "p", "1", "ffs", 8)  # 花火が上がる音


class FireworkParticle:  # 花火の粒子
    def __init__(self, x, y, angle, speed, color):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.color = color
        self.alive = True

    def update(self):
        self.x += self.speed * pyxel.cos(self.angle)
        self.y += self.speed * pyxel.sin(self.angle)
        self.speed *= 0.98  # 減速
        if self.speed < 0.3:
            self.alive = False  # 点が広がったら消える

    def draw(self):
        if self.alive:
            pyxel.pset(self.x, self.y, self.color)


class Firework:  # 花火
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.particles = []
        self.exploded = False  # 花火が開いたかどうか

    def update(self):
        if not self.exploded:  # 花火が開く前
            self.y -= 2
            if self.y < pyxel.rndi(40, 80):  # 花火が開く位置
                self.explode()  # 花火を開く
                pyxel.play(0, 0)  # 花火が開く音を鳴らす
        else:  # 花火が開いた後
            for particle in self.particles:
                particle.update()

    def explode(self):
        self.exploded = True
        for _ in range(100):  # 花火の粒子を配置
            angle = pyxel.rndi(0, 360)
            speed = pyxel.rndf(1, 2)
            # FireworkParticle クラスのインスタンスをリストに追加
            self.particles.append(
                FireworkParticle(self.x, self.y, angle, speed, self.color)
            )

    def draw(self):
        if not self.exploded:  # 花火が開く前
            pyxel.pset(self.x, self.y, self.color)  # まっすぐ上に上がる
        else:  # 花火が開いた後
            for particle in self.particles:  # 花火の粒子を描く
                particle.draw()


class App:
    def __init__(self):
        pyxel.init(180, 256, title="Fireworks")

        pyxel.sounds[0].set(*EXPLOSION_SOUND)  # 花火が開く音
        pyxel.sounds[1].set(*SHOOT_SOUND)  # 花火が上がる音

        self.fireworks = []
        self.launch_interval = 18
        self.launch_timer = 0

        pyxel.run(self.update, self.draw)

    def update(self):
        self.launch_timer += 1
        if self.launch_timer > self.launch_interval:
            self.launch_timer = 0
            self.launch_firework()
            pyxel.play(1, 1)  # 花火が上がる音を鳴らす

        for firework in self.fireworks:
            firework.update()

    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)
        for firework in self.fireworks:
            firework.draw()

    def launch_firework(self):  # 花火打ち上げ
        x = pyxel.rndi(20, pyxel.width - 20)  # 花火を打ち上げる位置
        y = 200
        color = pyxel.rndi(8, 12)  # 花火の色
        self.fireworks.append(Firework(x, y, color))


App()
