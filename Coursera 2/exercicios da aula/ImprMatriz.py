matriz = []
lin = int(input('Digite o número de linhas da matriz: '))
col = int(input('Digite o número de colunas da matriz: '))
for i in range(lin):
#cria a linha i
    linha =[] # lista vazia
    for j in range(col):
        valor = int(input('Digite o elemento [' + str(i) + '][' + str(j) + '] '))
        linha.append(valor)
    # adiciona linha à matriz
    matriz.append(linha)

def imprime_matriz(m):
    lin = len(m)
    col = len(m[0])   
    for li in range(lin):
        for co in range(col):
            print(f'{m[li][co]}', end=" ")
            if co == (col - 1):
                print( )
              

'''minha_matriz = matriz
imprime_matriz(minha_matriz)'''

print(imprime_matriz(matriz))
