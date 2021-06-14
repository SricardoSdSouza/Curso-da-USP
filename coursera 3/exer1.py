'''def cria_matriz(tot_lin, tot_col, valor):
    matriz = []  #lista vazia
    for i in range(tot_lin):
        linha = []
        for j in range(tot_col):
            linha.append(valor)
        matriz.append(linha)
    return matriz
x= cria_matriz(2,3,99)
print(x)


def tarefa(mat):
    dim = len(mat)
    for i in range(dim):
        print(mat[i][dim-1-i], end="  ")

mat = [[1,2,3],[4,5,6],[7,8,9]]
tarefa(mat)'''
 
def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_colunas):
        linha = []
        for j in range(num_linhas):
            valor = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz
print(cria_matriz(3,4))
