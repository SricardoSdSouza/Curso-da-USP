
def ordenação_por_seleção(lista):
    tamanho_da_lista = len(lista)
    for i in range(tamanho_da_lista -1):
        indice_menor_elemento =i
        
        for k, elemento_analisado in enumerate(lista[i+1:],start = i+1):
            if elemento_analisado < lista[indice_menor_elemento]:
                indice_menor_elemento = k
        if indice_menor_elemento != i:
            lista[indice_menor_elemento], lista[i] = (lista[i],lista[indice_menor_elemento])
    return lista


lista = [9,8,7,3,4,2,10,11,12,31,32,43,15,6,1,10,11,12,31,32,43,15,6,1]
print(ordenação_por_seleção(lista))
'''# saber o tempo de execussão
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
