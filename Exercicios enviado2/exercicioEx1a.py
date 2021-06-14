''' Programa para calcular a distância entre dois pontos.
onde:
x1 é a abscissa de A, y1 é a ordenada de A.
x2 é a abscissa de B, y2 é a ordenada de B.
'''
import math
x1 = float(input("Digite a abscissa do ponto A: "))
x2 = float(input("Digite a abscissa do ponto B: "))

y1 = float(input("Digite a ordenada do ponto A: "))
y2 = float(input("Digite a ordenada do ponto B: "))

X1=float((x1-x2)**2)
Y1=float((y1-y2)**2)

d=math.sqrt(X1+Y1)

if d >=10:
    print("Longe")
else:
    print("Perto")
