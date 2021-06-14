# matrizes
#a = [[1, 2, 3],[3, 5, 6],[7, 8, 9]]

def cria_matriz(num_linhas, num_colunas):
    """ (int, int) -> matriz (lista de listas)
    cria e retorna uma matriz comnum_linhas linhas e num_colunas
    colunas em que cada elemento é digitado pelo usuário.
    """
    matriz = [] # lista vazia
    for i in range(num_linhas):
        #cria a linha i
        linha =[] # lista vazia
        for j in range(num_colunas):
            valor = int(input('Digite o elemento [' + str(i) + '][' + str(j) + '] '))
            linha.append(valor)
        # adiciona linha à matriz
        matriz.append(linha)
    return matriz

def le_matriz():
    lin = int(input('Digite o número de linhas da matriz: '))
    col = int(input('Digite o número de colunas da matriz: '))
    return cria_matriz(lin, col)



m = le_matriz()
for i in m:
    print(i,end='')

