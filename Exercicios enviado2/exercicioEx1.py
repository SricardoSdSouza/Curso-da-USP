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

'''calculando a distância'''

distAB =int(math.sqrt(((x1)-(x1))**2) + (((y1)-(y2))**2))
print(distAB)
if distAB >=10:
    print("Longe")
else:
    print("Perto")

print("a distancia entre estes dois pontos é de =",distAB)
