#'soma'
def somar(m1, m2):
    matriz_soma = []
    # Supondo que as duas matrizes possuem o mesmo tamanho
    quant_linhas = len(m1) # Conta quantas linhas existem
    quant_colunas = len(m1[0]) # Conta quantos elementos têm em uma linha
    for i in range(quant_linhas):
        # Cria uma nova linha na matriz_soma
        matriz_soma.append([])
        for j in range(quant_colunas):
            # Somando os elementos que possuem o mesmo índice
            soma = m1[i][j] + m2[i][j]
            matriz_soma[i].append(soma)
    return matriz_soma

def mult_escalar(matriz,escalar):
    matriz_mult = []
    quant_linhas = len(matriz) # Conta quantas linhas existem
    quant_colunas = len(matriz[0]) # Conta quantos elementos têm em uma linha
    for i in range(quant_linhas):
        # Cria uma nova linha na matriz_mult
        matriz_mult.append([])
        for j in range(quant_colunas):
            # Multiplicando cada elemento pelo escalar
            mult = escalar * matriz[i][j]
            matriz_mult[i].append(mult)
    return matriz_mult


#multiplicação entre matrizes
def matriz_mult(a, b):
    linhaA, colunaA = len(a), len(a[0])
    linhaB, colunaB = len(b), len(b[0])
    if colunaA != linhaB:
        print(f"Não é possível calcular a multiplicação. Matriz A tem {colunaA} colunas, matriz B tem {linhaB} linhas")
        return []

    r = []
    for i in range(linhaA):
        r.append([0] * colunaB)  # Adiciona uma linha nova e gera todas as colunas dessa linha
        for j in range(colunaB):
            for k in range(colunaA):  # pode usar também linhaB, já que nesse ponto elas são iguais
                r[i][j] += a[i][k] * b[k][j]
    return r


def matriz_nula(nlinhas, ncols):
    M = []
    for i in range(nlinhas):
        linha = [0]*ncols
        M.append(linha)
    return M

def transposta(M):
    nlinhas = len(M)  # Conta quantas linhas existem
    ncolunas = len(M[0])  # Conta quantos elementos têm em uma linha
    T = matriz_nula(ncolunas, nlinhas)
    for i in range(nlinhas):
        for j in range(ncolunas):
            T[j][i] = M[i][j]
    return T


#matriz inversa
    
def matriz_inversa2(m):
    det = det_matriz(m)
    if det == 0:
        print ("Determinte igual a zero")
        return []
    a = 1/det
    b = mult_escalar (matrix_tamplate(m),a)
   
    return b

def matrix_tamplate(m): #cria o formato da matriz
    resultado = [[0, 0],[0, 0]]
    resultado [0][0] = m[1][1]
    resultado [0][1] = - m[0][1]
    resultado [1][0] = - m[1][0]
    resultado [1][1] = m[0][0]

    return resultado



#função de subtração entre duas matrizes
def subtrair(a,b): 
    return somar(a,mult_escalar(b,-1))
    


def informar_matriz():
    m = int (input ("Digite a quantidade de itens das linhas:")) 
    n = int (input ("Digite a quantidade de itens das colunas"))    
    matriz=[]
    for i in range (m): #varrendo os itens da linha 
        matriz.append([0]*n) #cria a linha corrente mais as colunas
        for j in range (n): #varrendo as colunas
            matriz[i][j] = int (input (f"Digite o valor do elemento {i+1},{j+1}: ")) #pedindo as valores da matriz e atribuindo na posição correta
    return matriz 

"""
    matriz: matriz original 
    linha: linha do pivo 
    col: coluna do pivo
"""
def cria_matriz_cofator(matriz, linha, col):
    tam = len(matriz) # lendo as quantidades de linha na matriz 
    tam_nova = tam -1 
    matriz_nova = []
    l_nova = 0
    for l in range(tam): 
        if l != linha: # não consedera a linha aonde está o pivo
            matriz_nova.append([0]*tam_nova)
            c_nova = 0
            for c in range(tam):
                if c != col: # não considera a coluna aonde está o pivo
                    matriz_nova[l_nova][c_nova] = matriz[l][c] 
                    c_nova += 1
            l_nova += 1

    return matriz_nova


"""
    Resolução de determinante por Teorema de Laplace
"""
def det_matriz(matriz):
    tam = len(matriz)

    # condição de parada da recursão
    if tam == 1:
        return matriz[0][0]
    
    #inicio do calculo
    col = 0 # fixando coluna em 0
    soma = 0 
    for linha in range(tam): 
        item = matriz[linha][col] # pegando os elementos da coluna 0
        if item != 0:  #se o item igual a zero não realiza o calculo
            mult = (-1)**(linha+col) # potencia do co-fator
            soma += mult * item * det_matriz(cria_matriz_cofator(matriz, linha, col)) # calculo recursivo do co-fator

    return soma

def verifica_matriz(matriz):
    tam_linha = len(matriz) 
    for linha in range (tam_linha):
        tam_col = len(matriz[linha])
        if tam_linha != tam_col: 
            return False # se coluna diferente de linhas retorna falso
    return True

def imprimir_determinante(matriz):
    matriz_quadrada = verifica_matriz(matriz)
    if matriz_quadrada == True:
        det = det_matriz (matriz)
        print(f"Velor da determinante é: {det}") 
    else: 
        print("Matriz não é quadrada!")
