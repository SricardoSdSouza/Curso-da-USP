
'''def x(n, m):
    if n == m or m == 0:
        return 1
    else:
        return x(n-1,m) + x(n-1,m+1)

print(x(5,3))'''

'''def x(n):
    #r,r1 = 0
    if n >= 0 or n <= 2:
        #r += 1
        return n
    else:
        #r1 += 1
        return x(n-1) + x(n-2) + x(n-3)

print(x(6))'''

def busca_binaria(lista, elemento, min=0, max=None):
    if max == None:
        max = len(lista)-1

    if max < min:
        return False
    else:
        meio = min + (max-min)//2

    if lista[meio] > elemento:
        return busca_binaria(lista, elemento, min, meio - 1)
    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, meio + 1, max)
    else:
        return meio

a = [-10, -2, 0, 5, 66, 77, 99, 102, 239, 567, 875, 934]
print(busca_binaria(a,(99)))
