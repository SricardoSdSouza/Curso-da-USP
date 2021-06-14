
def busca(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            letra = i  
            return letra
    return False

 
'''list = ['a', 'e', 'l']
print(busca(list,'e'))
lista = [12,13,14]
print(busca(lista, 15))'''
