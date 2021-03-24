from funcoes import *

def lista_exercicios_matriz():
    Matriz_A = [[2, 1], [-3, 4]]
    Matriz_B = [[0, -1], [2, 5]]
    Matriz_C = [[3, 0],[6, 1]]

  
    #Resposta questão 1#
    print(f"Resultado questão 1:\n {matriz_mult(Matriz_A, Matriz_B)}\n")
    
    #Resposta  2 (A+b) + (4*c)#
    r2 = somar(somar(Matriz_A, Matriz_B), mult_escalar(Matriz_C,4))
    print(f"Resultado questão 2:\n {r2}\n")

    #Resposta 3 [A+(B-Ct])*B-1]#
    r3 = subtrair(Matriz_B,transposta(Matriz_C))
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

def lista_exercios_determinante():
    pass

if __name__ == '__main__':
    # lista_exercicios_matriz()
    #lista_exercicios_determinate()
    
    
     """matriz = informar_matriz()
     imprimir_determinante(matriz)
     """
     Matriz_A = [[1, -1, 0], [2, 3, 4],[0, 1, -2]]
     Matriz_B = [[2, 7, 2], [8, -1, -3],[-1, 9, 5]]

     det_a = det_matriz(Matriz_A)
     trans_a = transposta(Matriz_A)
     soma_b_at = somar(Matriz_B,trans_a)
     print(soma_b_at)
     final = mult_escalar(soma_b_at,det_a)
     print(f"Resultado questão 2:\n {final}")