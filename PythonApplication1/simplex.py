import math

import funcoes as F


def def_entra_base(coeficientes_objetivo):
    lin = 0
    col = 0
    menor_elemento = coeficientes_objetivo[lin][col]

    tam_linha = len(coeficientes_objetivo)
    for l in range(tam_linha):
        tam_coluna = len(coeficientes_objetivo[l])
        for c in range(tam_coluna):
            atual = coeficientes_objetivo[l][c]
            if atual < menor_elemento:
                lin = l
                col = c
                menor_elemento = atual

    return lin, col, -1 * menor_elemento


def def_sai_base(coeficiente_resticoes, termos_independentes, col_pivo):
    tam_linha = len(coeficiente_resticoes)
    valores = [0] * tam_linha
    for l in range(tam_linha):
        pivo = coeficiente_resticoes[l][col_pivo]
        ind = termos_independentes[l][0]
        if pivo > 0:
            valores[l] = ind / pivo
        else:
            valores[l] = math.inf

    ind = 0
    val = valores[ind]
    for i, v in enumerate(valores):
        if v < val:
            ind = i
            val = v

    return ind, val


def trocar_coluna(matriz_origem, coluna_deve_trocar, matriz_destino, coluna_vai_trocar):
    result = []
    for l in range(len(matriz_origem)):
        linha = []
        result.append(linha)
        for c in range(len(matriz_destino)):
            if c == coluna_deve_trocar:
                linha.append(matriz_destino[l][coluna_vai_trocar])
            else:
                linha.append(matriz_origem[l][c])

    return result


def verificar_valores_negativos(matriz):
    for l in matriz:
        for item in l:
            if item < 0:
                return True
    return False


def informar_matriz_restricoes(x):
    n = int(input("Quantas restrições:"))
    matriz = []
    for i in range(x):  # varrendo os itens da linha
        matriz.append([0] * n)  # cria a linha corrente mais as colunas
        for j in range(n):  # varrendo as colunas
            matriz[i][j] = int(input(
                f"Digite o valor do elemento {i + 1},{j + 1}: "))  # pedindo as valores da matriz e atribuindo na posição correta
    return matriz, n


def informar_funcao_objetivo(m):
    print("Informe os coeficieentes da função objetivo: ")
    linha = []
    for i in range(m):  # varrendo os itens da linha
        valor = float(input())  # pedindo as valores da matriz e atribuindo na posição correta
        linha.append(valor)
    matriz = []
    matriz.append(linha)
    return matriz


def informar_termos_independentes(n):
    print("Informe os termos independentes: ")
    linha = []
    for i in range(n):  # varrendo os itens da linha
        valor = float(input()) # pedindo as valores da matriz e atribuindo na posição correta
        linha.append(valor)
    matriz = []
    matriz.append(linha)
    return matriz

def exemplo_manual():
    m = int(input("Quantas variaveis de decisão tem o problema:"))
    C = informar_funcao_objetivo(m)  #
    A, n = informar_matriz_restricoes(m)
    D = informar_termos_independentes(n)

    return m, C, A, n, D

def exemplo_1():
    C =  [[1, 4, 2]]
    m = len(C[0])
    A = [[2, 2, 0], [1, 0, 3], [1, 1, 2]]
    n = len(A)
    D = [[20, 15, 40]]
    return m, C, A, n, D

def exemplo_2():
    C = [[4, 1]]
    m = len(C[0])
    A = [[9, 1], [3, 1]]
    n = len(A)
    D = [[18, 12]]
    return m, C, A, n, D

if __name__ == '__main__':
    # m = int(input("Quantas variaveis de decisão tem o problema:"))
    # C = informar_funcao_objetivo(m)  # [[1, 4, 2]]
    # A, n = informar_matriz_restricoes(m)
    # D = informar_termos_independentes(n)

    m, C, A, n, D = exemplo_1()
    #simplex
    b = F.transposta(D)
    X = F.transposta([[f'x{i}' for i in range(1, m + 1)]])
    Xb = F.transposta([[f'S{i}' for i in range(1, n + 1)]])

    B = F.gerar_identidade(n)

    Cb = [[0]*n]

    # Definir variaveis de base

    # Definir quem entra na base
    C1 = F.mult_escalar(C, -1)
    while verificar_valores_negativos(C1):
        l, coluna_entrada, valor_entrada = def_entra_base(C1)
        entra_na_base = F.transposta(X)[l][coluna_entrada]

        # Definir quem sai da base
        linha_saida, val = def_sai_base(A, b, coluna_entrada)
        Xb[linha_saida][0] = entra_na_base

        B = trocar_coluna(
            # Bug
            B,
            linha_saida,
            A,
            coluna_entrada
        )
        Bi = F.matriz_inversa(B)
        Cb[0][linha_saida] = valor_entrada

        matriz_opera = F.matriz_mult(Cb, Bi)
        matriz_opera = F.matriz_mult(matriz_opera, A)
        matriz_opera = F.somar(matriz_opera, C1)
        C1 = matriz_opera

        matriz_opera2 = F.matriz_mult(Cb, Bi)

    Rb = F.matriz_mult(Bi, b)
    Z = F.matriz_mult(Cb, Bi)
    Z = F.matriz_mult(Z, b)
    print(Z)
