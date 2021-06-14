def sao_multiplicaveis(n1, n2):
    n1_cols = len(n1[0])
    n2_rows = len(n2)
    return (n1_cols == n2_rows)

a = [[1,2,3],[4,5,6]]
b = [[2, 3, 4], [5, 6, 7]]
print(sao_multiplicaveis(a,b))
a = [[1], [2], [3]]
b = [[1, 2, 3]]
print(sao_multiplicaveis(a,b))
