import pyxel

pyxel.init(80, 64)
pyxel.load("my_resource.pyxres")

pyxel.cls(1)
pyxel.blt(5, 5, 0, 8, 0, 8, 8, 0)
pyxel.blt(20, 5, 0, 8, 0, 8, 8, 11)
pyxel.blt(35, 5, 0, 8, 0, 8, 4, 0)

pyxel.show()
