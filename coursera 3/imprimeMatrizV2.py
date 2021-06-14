
def imprime_matriz(m):
    lin = len(m)
    col = len(m[0])   
    for li in range(lin):
        for co in range(col):
            if co < (col - 1):
                print(f'{m[li][co]}',end=' ')
            else:
                print(m[li][co])


'''minha_matriz = [[1,2,3],[4,5,6]]
imprime_matriz(minha_matriz)
minha_matriz = [[1],[2],[3]]
imprime_matriz(minha_matriz)'''
