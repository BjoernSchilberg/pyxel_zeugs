import pyxel

# https://gist.github.com/fabiommendes/a1e9f86eb828f728e2590ee406fef700

# Constantes
RAIO = 2
ALTURA = 12  # altura de cada pá
LARGURA = 2  # largura de cada pá
P1_X = 3
P2_X = 120 - 3
FPS = 30
dt = 1 / FPS

# Variáveis que descrevem o estado do jogo
x, y = 120 / 2, 80 / 2
vx, vy = 21, 21
p1_y = 80 / 2
p2_y = 80 / 2
p1_pontos = 0
p2_pontos = 0
pausado = True


# =============================================================================
# Implementa a lógica do jogo
# =============================================================================
def update():
    global x, y, vx, vy, p1_y, p2_y, p1_pontos, p2_pontos, pausado

    # Modifica a posição dos jogadores de acordo com o teclado
    p1_y = move_jogador(p1_y, pyxel.KEY_W, pyxel.KEY_S)
    p2_y = move_jogador(p2_y, pyxel.KEY_UP, pyxel.KEY_DOWN)

    # Aplica velocidade à bola
    if not pausado:
        x = x + vx * dt
        y = y + vy * dt
    elif pausado and pyxel.btnp(pyxel.KEY_SPACE):
        pausado = False

    # Implementa colisão com as paredes
    if y <= RAIO + 1 or y >= 80 - (RAIO + 1):
        vy *= -1

    # Implementa colisão com os jogadores
    vx_mul = 1.0
    if x <= P1_X + LARGURA / 2 + RAIO and abs(y - p1_y) < RAIO + ALTURA / 2:
        vx_mul = -1
    if x >= P2_X - LARGURA / 2 - RAIO and abs(y - p2_y) < RAIO + ALTURA / 2:
        vx_mul = -1
    vx *= vx_mul

    # Verifica se o P1 perdeu
    if x < 0:
        p2_pontos += 1
        x, y = 120 / 2, 80 / 2
        pausado = True
    # Verifica se o P2 perdeu
    if x > 120:
        p1_pontos += 1
        x, y = 120 / 2, 80 / 2
        pausado = True


def move_jogador(y, cima, baixo):
    if pyxel.btn(cima):
        y -= 1
    elif pyxel.btn(baixo):
        y += 1
    y = max(y, ALTURA / 2 + 1)
    y = min(y, 80 - ALTURA / 2 - 1)
    return y


# =============================================================================
# Desenha elementos da tela
# =============================================================================
def draw():
    pyxel.cls(pyxel.COLOR_BLACK)

    # Desenha os dois jogadores e a bola
    desenha_jogador(P1_X, p1_y, p1_pontos, "esquerda")
    desenha_jogador(P2_X, p2_y, p2_pontos, "direita")
    pyxel.circ(x, y, RAIO, pyxel.COLOR_RED)

    # Desenha borda da tela
    pyxel.line(0, 0, 120, 0, pyxel.COLOR_WHITE)
    pyxel.line(0, 79, 120, 79, pyxel.COLOR_WHITE)

    if pausado:
        pyxel.text(35, 40, "aperte espaco", pyxel.COLOR_YELLOW)


def desenha_jogador(pos_x, pos_y, pontos, alinhamento):
    x = pos_x - LARGURA / 2
    y = pos_y - ALTURA / 2
    pyxel.rect(x, y, LARGURA, ALTURA, pyxel.COLOR_WHITE)

    # Desenha o placar
    txt = str(pontos)
    x = pos_x
    y = 3
    if alinhamento == "direita":
        x -= len(txt) * pyxel.FONT_WIDTH
    pyxel.text(x, y, txt, pyxel.COLOR_WHITE)


# =============================================================================
# Inicializa o Pyxel
# =============================================================================
pyxel.init(120, 80, fps=FPS)
pyxel.mouse(True)
pyxel.run(update, draw)
