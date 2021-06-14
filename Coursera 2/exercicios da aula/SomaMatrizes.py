def cria_matriz(num_linhas, num_colunas, valor):
    """ (int, int, valor) -> matriz (lista de listas)
    cria e retorna uma matriz comnum_linhas linhas e num_colunas
    colunas em que cada elemento é igual ao valor dado.
    """
    matriz = [] # lista vazia
    for i in range(num_linhas):
        #cria a linha i
        linha =[] # lista vazia
        for j in range(num_colunas):
            linha.append(valor)

        # adiciona linha à matriz
        matriz.append(linha)
    return matriz

def soma_matrizes(a, b):
    num_lin = len(a)
    num_col = len(a[0])#Ocomprimento da coluna inicial será a primeira linha de a
    c = cria_matriz(num_lin, num_col, 0 )
    for lin in range(num_lin): #percorre as linhas da matriz
        for col in range(num_col):# percorre as colunas da matriz
                c[lin][col] = a[lin][col] + b[lin][col]
    return c

m1 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
m2 = [[10, 20, 30],[40, 50, 60],[70, 80, 90]]
print(soma_matrizes(m1, m2))


