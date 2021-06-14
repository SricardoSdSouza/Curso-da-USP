import math

numero = int(input('numero: '))
n=int(numero)
if numero > 0:
    soma = 0
    while numero != 0:
        resto = numero % 10
        numero = (numero - resto) // 10
        soma = soma + resto
    print("A soma dos números(",n,")é = ",soma)
else:
    print('Número invalido...')
