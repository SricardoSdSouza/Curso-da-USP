# matrizes
#a = [[1, 2, 3],[3, 5, 6],[7, 8, 9]]

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


