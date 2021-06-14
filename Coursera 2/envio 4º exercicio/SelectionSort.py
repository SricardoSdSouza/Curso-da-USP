
def  ordena(lista):
    
    for i in range(0, len(lista)):
        menor = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        lista[i],lista[menor] = lista[menor],lista[i]

