import random

def encontrar_menor_elemento(lista):
    indice_menor_elemento = 0
    menor_elemento = lista[indice_menor_elemento]
    
    for i, elemento in enumerate(lista[1:],start = 1):
        if elemento < menor_elemento:
            menor_elemento = elemento
            indice_menor_elemento = i
            
    return indice_menor_elemento


def ordena(lista_d):
    lista_ordenada = []
    tamanho_da_lista = len(lista_d)
    for _ in range(tamanho_da_lista):
        indice_menor_elemento = encontrar_menor_elemento(lista_d)
        lista_ordenada.append(lista_d.pop(indice_menor_elemento))
    return lista_ordenada


'''lista = [9,8,7,3,4,2,10,11,12,31,32,43,15,6,1]
print(ordena(lista))
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
