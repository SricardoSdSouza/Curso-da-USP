'''def cria_matriz(tot_lin, tot_col, valor):
	matriz = []
	for i in range(tot_lin):
		linha = []
		for j in range(tot_col):
		    linha.append(valor)
		matriz.append(linha)
	return matriz

cria_matriz(1, 3, 99)
m = cria_matriz()'''


'''def tarefa(mat):
    dim = len(mat)
    for i in range(dim):
        print(mat[i][dim-1-i],end=' ')

mat = [[1,2,3,],[4,5,6,],[7,8,9]]
tarefa(mat)'''

def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz
x = cria_matriz(2,3)
print('A 1º matriz',x)

def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_colunas):
        linha = []
        for j in range(num_linhas):
            valor = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

x = cria_matriz(2,3)
print('A 2º matriz',x)

# imprime primeiro a primeira coluna depois a segunda coluna
def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(0)
        matriz.append(linha)

    for i in range(num_colunas):
        for j in range(num_linhas):
            matriz[j][i] = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))

    return matriz

x = cria_matriz(2,3)
print('A 3º matriz',x)

'''def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        coluna = []
        for j in range(num_colunas):
            coluna.append(0)
        matriz.append(coluna)

    for i in range(num_linhas):
        for j in range(num_colunas):
            matriz[j][i] = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]: "))

    return matriz
x = cria_matriz(2,3)
print('A 4º matriz',x)'''

def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_colunas):
        coluna = []
        for j in range(num_linhas):
            valor = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))
            coluna.append(valor)
        matriz.append(coluna)
    return matriz

x = cria_matriz(2,3)
print('A 5º matriz',x)

