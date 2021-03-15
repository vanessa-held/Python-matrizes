

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
def determinante_matriz2(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]
    
def matriz_inversa2(m):
    det = determinante_matriz2(m)
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
    

if __name__ == '__main__':

    Matriz_A = [[2, 1], [-3, 4]]
    Matriz_B = [[0, -1], [2, 5]]
    Matriz_C = [[3, 0],[6, 1]]

  
    #Resposta questão 1#
    print(f"Resultado questão 1:\n {matriz_mult(Matriz_A, Matriz_B)}\n")
    
    #Resposta  2 (A+b) + (4*c)#
    r2 = somar(somar(Matriz_A, Matriz_B), mult_escalar(Matriz_C,4))
    print(f"Resultado questão 2:\n {r2}\n")

    #Resposta 3 [A+(B.Ct])*B-1]#
    r3 = matriz_mult(Matriz_B,transposta(Matriz_C))
    r3 = somar(Matriz_A,r3)
    r3 = matriz_mult(r3,matriz_inversa2(Matriz_B))
    print(f"Resultado questão 3:\n {r3}\n")
  

    #Resposta 4 (A*A-1) = In#
    r4 = matriz_mult(Matriz_A,matriz_inversa2(Matriz_A))
    print(f"Resultado questão 4:\n {r4}\n")
    print(f' Resultado Matriz inversa: \n{matriz_inversa2(Matriz_A)}')

    #Resposta  (b + At * C-1 -Bt) = In#
    r5 = matriz_mult(transposta(Matriz_A), matriz_inversa2(Matriz_C)) # At*C-1
    r5 = somar(Matriz_B,r5)
    r5 = subtrair(r5,transposta(Matriz_B))
    print (f"Resultado questão 5:\n {r5}\n")



 
