def sao_multiplicaveis(m1, m2):
    num_linhas_a, num_colunas_a = len(a), len(a[0])
    num_linhas_b, num_colunas_b = len(b), len(b[0])
    assert num_colunas_a == num_linhas_b
    c = []
    for linha in range(num_linhas_a):
        c.append([])# inicio de nova linha
        for coluna in range(num_colunas_b):
            c[linha].append(0)#adicionando uma nova coluna na linha
            for k in range(num_colunas_a):
                c[linha][coluna] += a[linha][k] * b[k][coluna]
    return c

if __name__== '__main__':
    a = [[2,2,2],[4,4,4]]
    b = [[1,1],[2,2],[3,3],[7,7]]
    print(sao_multiplicaveis(a,b))
