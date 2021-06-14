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

def imprime_matriz(matriz):

    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        for j in range(colunas):
            if(j == colunas - 1):
                print("%d" %matriz[i][j])
            else:
                print("%d" %matriz[i][j],end=" ")
                
    print()

'''def imprime_matriz(m): 
    for li in m:
        for val in li:
               print(f'{val}')'''


m = minha_matriz()
#m = [[1],[2],[3]]
imprime_matriz(m)
