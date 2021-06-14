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

def minha_matriz():
    lin = int(input('Digite o número de linhas da matriz: '))
    col = int(input('Digite o número de colunas da matriz: '))
    return cria_matriz(lin, col)


def imprime_matriz(m):
    lin = len(m)
    col = len(m[0])   
    for li in range(lin):
        for co in range(col):
            print(f'{m[li][co]}',end=' ')
            if co == (col -1):
                print('')


minha_matriz = [[1,2,3],[4,5,6]]
imprime_matriz(minha_matriz)
minha_matriz = [[1],[2],[3]]
imprime_matriz(minha_matriz)
