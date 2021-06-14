from random import random, randint

def lista_grande(n):
    numeros = n
    list = [n] * numeros
    for i in range(numeros):
        list[i] = randint(i,n)
    return list


print(lista_grande(5))
