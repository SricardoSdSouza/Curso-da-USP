def mat_mul(A, B):
    try:
        num_linhas_A, num_colunas_A = len(A), len(A[0])
        num_linhas_B, num_colunas_B = len(B), len(B[0])
        assert num_colunas_A == num_linhas_B
    except AssertionError:
        print('Não é possível fazer a multiplicação')

    C = []
    for linha in range(num_linhas_A):
        C.append([])# inicio de nova linha vazia
        for coluna in range(num_colunas_B):
            C[linha].append(0)#adicionando uma nova coluna na linha
            for k in range(num_colunas_A):
                C[linha][coluna] += A[linha][k] * B[k][coluna]
    return C

if __name__== '__main__':
    A = [[1,2,3],[4,5,6]]
    B = [[1,2],[3,4],[5,6],[5,6]]
    print(mat_mul(A, B))
