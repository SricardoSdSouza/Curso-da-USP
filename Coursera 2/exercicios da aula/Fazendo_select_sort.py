import random
import time

def selection_sort(v):
    i = 0
    while i < len(v)-1:
        menor = i
        j = i + 1
        #em busca do menor elemento
        while j < len(v):
            if v[j] < v[menor]:
                menor = j
            j += 1
        # verifica se precisa realizar a troca
        if menor != i:
            temp = v[i]
            v[i] = v[menor]
            v[menor] = temp
        i += 1



'''lista = [9,8,7,3,4,2,10,11,12,31,32,43,15,6,1]
antes =time.time()
selection_sort(lista)
depois = time.time()
# saber o tempo de execussão
total = (depois - antes)*1000
print(lista)
print(f'total = {total:.18f}')
print('=-='*10)
lista1 = [1,2,3,4,5,6]
selection_sort(lista1)
print(lista1)
print('=-='*10)
lista2 = [1,6,2,4,7,3]
selection_sort(lista2)
print(lista2)
print('=-='*10)
lista3 = [10,30,20,60,50,40]
selection_sort(lista3)
print(lista3)
print('=-='*10)
lista4 = [1,-2,3,4,5,6]
selection_sort(lista4)
print(lista4)
print('=-='*10)'''
