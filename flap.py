# https://gist.github.com/fabiommendes/06dc57956320bf8d8fb33ee9ff33d3e4
import pyxel
from random import randint

# Declara variáveis globais

# Posição e velocidade
x = 20
y = 40
vy = -20

# Gravidade
g = 15

# Duração do frame
fps = 30
dt = 1 / fps  # duração de cada frame

# Guarda score e se o jogo está perdido ou não
game_over = False
score = 0

# Posições (x, h) do canto inferior esquerdo de cada
# par de canos.
# Usa o cano superior como referência
canos_xs = [50, 90, 130, 170]
canos_hs = [10, 25, 15, 5]


def update():
    global x, y, vy, game_over, canos_xs, score

    # Não atualizamos a física de um jogo perdido.
    # Podemos fazer isso simplesmente retornando a
    # função prematuramente
    if game_over and pyxel.btnp(pyxel.KEY_SPACE):
        # Reinicia o jogo
        y = 40
        vy = -20
        game_over = False
        canos_xs = [50, 90, 130, 170]
        score = 0
    elif game_over:
        # Mantêm o jogo pausado
        return

    # Atualiza a posição e velocidade do passarinho
    # de acordo com as leis da física de movimento
    # acelerado
    # s = s0 + v0 * t + a*t**2/2
    # v = v0 + a * t
    y = y + vy * dt + g * dt**2 / 2
    vy = vy + g * dt

    # Verifica se o jogador apertou espaço
    # para causar um pulo
    if pyxel.btnp(pyxel.KEY_SPACE):
        vy = -20

    # Atualiza a posição x dos canos
    for i in range(len(canos_xs)):
        canos_xs[i] -= 0.5

    # Recicla os canos, se necessário
    if canos_xs[0] < -10:  # (10 = L, largura do cano)
        del canos_xs[0]
        del canos_hs[0]
        canos_xs.append(canos_xs[-1] + 40)  # cria um novo cano 40px após o último cano
        canos_hs.append(randint(5, 30))  # sorteia uma altura aleatória para ele
        score += 1

    # Verifica colisões
    for i in range(int(x), int(x + 5)):
        for j in range(int(y), int(y + 4)):
            if pyxel.pget(i, j) == pyxel.COLOR_LIME:
                game_over = True


def draw():
    # Limpa a tela
    pyxel.cls(pyxel.COLOR_BLACK)

    # Desenha o passarinho
    pyxel.rect(x + 1, y, 4, 4, pyxel.COLOR_YELLOW)
    if vy < 0:
        pyxel.rect(x - 1, y + 2, 2, 2, pyxel.COLOR_YELLOW)
    else:
        pyxel.rect(x - 1, y, 2, 2, pyxel.COLOR_YELLOW)

    pyxel.rect(x + 4, y + 2, 2, 1, pyxel.COLOR_ORANGE)
    pyxel.rect(x + 3, y + 1, 1, 1, pyxel.COLOR_BLACK)

    # Desenhar os canos
    for x_cano, h_cano in zip(canos_xs, canos_hs):
        desenha_cano(x_cano, h_cano)

    # Desenha o "game over"
    if game_over:
        pyxel.text(38, 40, "GAME OVER", pyxel.COLOR_WHITE)

    # Desenha o score
    pyxel.text(100, 5, f"n: {score}", pyxel.COLOR_WHITE)


def desenha_cano(x, h):
    cor = pyxel.COLOR_LIME
    L = 10
    B = 40

    # Cano de cima
    pyxel.rect(x, 0, L, h, cor)

    # Cano de baixo
    pyxel.rect(x, h + B, L, pyxel.height - (h + B), cor)


pyxel.init(120, 80, fps=fps)
pyxel.mouse(True)
pyxel.run(update, draw)
