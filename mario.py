import pyxel

COLORS = {
    "B": 5,  # Blue
    "K": 0,  # Black
    "O": 15,  # Orange
    "R": 8,  # Red
    "T": 9,  # Brown
    "W": 7,  # White
    "Y": 10,  # Yellow
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
