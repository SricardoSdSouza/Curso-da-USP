def imprime_matriz(m):
    lin = len(m)
    col = len(m[0])   
    for li in range(lin):
        for co in range(col):
            print(f'{m[li][co]}', end=" ")
            if co == (col - 1):
                print( )
              
