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


if __name__ == '__main__':
    C = [[1, 4, 2]]
    X = F.transposta([["x1", "x2", "x3"]])
    b = F.transposta([[20, 15, 40]])
    Xb = F.transposta([["S1", "S2", "S3"]])

    A = [
        [2, 2, 0],
        [1, 0, 3],
        [1, 1, 2], ]

    B = F.gerar_identidade(3)

    Cb = [[0, 0, 0]]

    # Definir variaveis de base

    # Definir quem entra na base
    b2 = b
    C1 = F.mult_escalar(C, -1)
    while verificar_valores_negativos(C1):
        l, coluna_entrada, valor_entrada = def_entra_base(C1)
        entra_na_base = F.transposta(X)[l][coluna_entrada]

        # Definir quem sai da base
        linha_saida, val = def_sai_base(A, b2, coluna_entrada)
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



        b2 = F.matriz_mult(Bi, b2)

    Rb = F.matriz_mult(Bi, b)
    Z = F.matriz_mult(Cb, Bi)
    Z = F.matriz_mult(Z, b)
    print(Z)
