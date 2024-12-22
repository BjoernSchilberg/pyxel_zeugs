import pyxel

COLORS = {
    "B": 1,
    "K": 0,
    "O": 2,
    "R": 8,
    "T": 6,
    "W": 7,
    "Y": 10,
}

PIXELS = [
    "WWWRRRRRRWWWW",
    "WWRRRRRRRRRRW",
    "WWTTTOOOKOWWW",
    "WTOTOOOOKOOOW",
    "WTOTTOOOOKOOO",
    "WTTOOOOOKKKKW",
    "WWWOOOOOOOOWW",
    "WWRRBRRRRWWWW",
    "WRRRBRRBRRRWW",
    "RRRRBBBBRRRRW",
    "OORBYBBYBROOW",
    "OOOBBBBBBOOOW",
    "OOBBBBBBBBOOW",
    "WWBBBWWBBBWWW",
    "WTTTWWWWTTTWW",
    "TTTTWWWWTTTTW",
]

WIDTH, HEIGHT = len(PIXELS[0]), len(PIXELS)


pyxel.init(WIDTH, HEIGHT, title="Pixel Art")

pyxel.cls(0)

# Draw the pixels
for y, row in enumerate(PIXELS):
    for x, pixel in enumerate(row):
        color = COLORS.get(pixel, 0)  # Default color is black
        pyxel.pset(x, y, color)

pyxel.show()
