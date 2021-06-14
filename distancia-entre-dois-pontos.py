"""Programa em Python que calcula a distância entre dois pontos, dadas as suas coordenadas. 
Considerando os pontos A(x1;y1) e B(x2;y2).

x1 é a abscissa de A, y1 é a ordenada de A.
x2 é a abscissa de B, y2 a ordenada de B
"""

_author_ = "Edigley Alexandre"

# Importando biblioteca matemática para a função de raiz quadrada
from math import sqrt

# Inserido coordenadas dos pontos
xA = float(input('Digite a abscissa do ponto A:'))
xB = float(input('Digite a abscissa do ponto B:'))

yA = float(input('Digite a ordenada do ponto A:'))
yB = float(input('Digite a abscissa do ponto B:'))

# Calculando a distância
distAB = sqrt((xA-xB)**2) + ((yA-yB)**2)

# Mostrando resultado
print('A distância entre esses dois pontos é de:', distAB, 'unidades de medida')
