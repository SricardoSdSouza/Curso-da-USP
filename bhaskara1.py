print("Vamos calcular as raízes de uma equação de 2º grau")
'''
importando biblioteca de matematica
'''
import math
'''
atribuindo valor as variaveis solicitando pelo teclado
'''
a=float(input("Digite o coeficiente de a = "))
b=float(input("Digite o coeficiente de b = "))
c=float(input("Digite o coeficiente de c = "))


'''
calculando do delta 
'''
delta=b**2-4*a*c
r1=(-b + math.sqrt(delta))/(2*a)
r2=(-b - math.sqrt(delta))/(2*a)
'''
testar se delta = a zero
'''
if delta ==0:
   raiz1 =r1
   print("Existe somente uma raiz para esta equação.",raiz1)
else:
   if delta<0:
      print("Esta equação não possui numeros reais.")
   else:
      raiz1 =r1
      raiz2 =r2
      print("O resultado final")
      print(" 0 valor de x1=  ",raiz1,"O valor de x2 =",raiz2)
      print("As raizes são %.2f e %.2f"%(raiz1,raiz2))




