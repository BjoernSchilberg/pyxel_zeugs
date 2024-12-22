import pyxel

pyxel.init(128, 128, "Déplacement d'un carré")

# initialisation
v = {"x": 0}


def update():
    """
    Mise à jour de la position de l'objet.
    """
    v["x"] = (v["x"] + 1) % pyxel.width


def draw():
    """
    Dessin des éléments à l'écran.
    """
    pyxel.cls(0)
    pyxel.rect(v["x"], 10, 8, 8, 9)


pyxel.run(update, draw)
