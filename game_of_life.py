import pyxel
from copy import deepcopy

LARGURA = 80
ALTURA = 60

# Liga/desliga simulação
pausa = True

# Tabuleiro de booleanos mostrando as células preenchidas
life = [[False for i in range(LARGURA)] for j in range(ALTURA)]


def update_life(life):
    """
    Executa uma rodada da simulação e retorna uma cópia com
    o novo estado da simulação.
    """

    life_ = deepcopy(life)
    for j, linha in enumerate(life_):
        for i, celula in enumerate(linha):
            n = n_vizinhos(life, i, j)

            if celula and (n < 2 or n > 3):
                life_[j][i] = False
            elif not celula and n == 3:
                life_[j][i] = True

    return life_


def get_pos(M, i, j):
    """
    Retorna valor na posição i, j ou False se a
    posição for inválida
    """
    try:
        return M[j][i]
    except IndexError:
        return False


def n_vizinhos(M, i, j):
    """
    Calcula número de vizinhos ativos na posição i, j.
    """
    n = 0
    n += get_pos(M, i - 1, j - 1)
    n += get_pos(M, i - 1, j)
    n += get_pos(M, i - 1, j + 1)
    n += get_pos(M, i, j - 1)
    n += get_pos(M, i, j + 1)
    n += get_pos(M, i + 1, j - 1)
    n += get_pos(M, i + 1, j)
    n += get_pos(M, i + 1, j + 1)
    return n


#
# Funções update/draw do pyxel
#
def update():
    global pausa, life

    # Desenha/apaga células com o mouse
    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        i = pyxel.mouse_x
        j = pyxel.mouse_y
        if pyxel.btn(pyxel.KEY_CTRL):
            life[j][i] = False
        else:
            life[j][i] = True

    # Troca o estado pausado
    if pyxel.btnp(pyxel.KEY_SPACE):
        pausa = not pausa

    # Atualiza a simulação
    if not pausa and pyxel.frame_count % 4 == 0:
        life = update_life(life)


def draw():
    pyxel.cls(pyxel.COLOR_BLACK)

    # Desenha o tabuleiro
    for j, linha in enumerate(life):
        for i, celula in enumerate(linha):
            if celula:
                pyxel.pset(i, j, pyxel.COLOR_LIME)

    # Destaca a posição atual do mouse
    pyxel.pset(pyxel.mouse_x, pyxel.mouse_y, pyxel.COLOR_RED)

    # Desenha o símbolo de pausa
    if pausa:
        x = int(LARGURA / 2)
        y = int(ALTURA / 2)
        pyxel.line(x - 1, y - 1, x - 1, y + 1, pyxel.COLOR_RED)
        pyxel.line(x + 1, y - 1, x + 1, y + 1, pyxel.COLOR_RED)


pyxel.init(LARGURA, ALTURA)
pyxel.run(update, draw)
