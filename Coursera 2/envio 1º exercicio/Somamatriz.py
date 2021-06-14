import matriz

def soma_matrizes(a, b):
    num_lin = len(a)
    num_col = len(a[0])#Ocomprimento da coluna inicial será a primeira linha de a
    c = matriz.cria_matriz(num_lin, num_col, 0 )
    for lin in range(num_lin): #percorre as linhas da matriz
        for col in range(num_col):# percorre as colunas da matriz
            c[lin][col] = a[lin][col] + b[lin][col]
    return c

if __name__ == '__main__':
    a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    b = [[10, 20, 30],[40, 50, 60],[70, 80, 90]]
    print(soma_matrizes(a, b))

