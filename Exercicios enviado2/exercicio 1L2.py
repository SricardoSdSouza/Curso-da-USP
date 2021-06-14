import math
'testar se o número é par'
numero = float(input ("Digite um número para ser testado se Par ou Ímpar "))
resto = numero%2
if resto==0:
    print(numero,"é um número é par")
else:
    print(numero," é número é impar")
