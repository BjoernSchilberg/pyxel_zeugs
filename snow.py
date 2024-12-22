import pyxel, random

pyxel.init(128, 128, title="Il neige!")

# initialisation
v = {"flocons": []}


def flocon_creation(flocons):
    """création aléatoire des flocons"""

    # Un flocon toutes les 15 frames (~2 flocons par seconde si Pyxel tourne à 30 FPS)
    if pyxel.frame_count % 15 == 0:
        v["flocons"].append([random.randint(0, 127), 0])


def flocon_deplacement(flocons):
    """déplacement des flocons vers le bas et suppression s'ils sortent de la fenêtre"""

    for flocon in v["flocons"]:
        flocon[1] += 1
        if flocon[1] > 128:
            v["flocons"].remove(flocon)


# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    # création des flocons
    flocon_creation(v["flocons"])

    # mise à jour des positions des flocons
    flocon_deplacement(v["flocons"])


# =========================================================
# == DRAW
# =========================================================
def draw():
    """Dessine la fenêtre et les flocons (30 fois par seconde)"""

    # nouvelle fenêtre bleue
    pyxel.cls(5)

    # affichage des flocons
    for flocon in v["flocons"]:
        pyxel.pset(int(flocon[0]), int(flocon[1]), 7)


pyxel.run(update, draw)
