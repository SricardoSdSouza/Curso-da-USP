import math

import math
va_n=int(input("Digite o numero para n = "))
va_k=int(input("Digite o numero para k = "))
n=va_n
k=va_k

def fatorial(n):
        fat = 1
        while (n>1):
                fat = fat*n
                n = n-1
        return fat

def numero_binomial(n,k):
        n=int(va_n)
        k=int(va_k)
        return fatorial(n)/(fatorial(k)*(fatorial(n-k)))

print("O binomial para este valores de = ","\nn = ",n," e ","k = ",k,"\n o resultado é = ",numero_binomial(int,int))

def testa_fatorial():
        if fatorial(1)==1:
                print("Funciona para 1")
        else:
                print("Não funciona para 1")
        if fatorial(2)==1:
                print("Funciona para 2")
        else:
                print("Não funciona para 2")
        if fatorial(0) ==1:
                print("Funciona para 0")
        else:
                print("Não funciona para 0")
        if fatorial(5)==120:
                print("funciona para 5")
        else:
                print("Não funciona para 5")

def calcular_pagamento(qtd_horas, valor_hora):
  horas = float(qtd_horas)
  taxa = float(valor_hora)
  if horas <= 40:
    salario=horas*taxa
  else:
    h_excd = horas - 40
    salario = 40*taxa+(h_excd*(1.5*taxa))
  return salario
