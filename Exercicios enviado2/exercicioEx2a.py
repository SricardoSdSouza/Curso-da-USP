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
'''
testar se delta = a zero
'''
if delta ==0:
   raiz1 =float((-b + math.sqrt(delta))/(2*a))
   print("A raiz desta equação é ",raiz1)
else:
   if delta<0:
      print("Esta equação não possui raízes reais.")
   else:
      raiz1 =int((-b + math.sqrt(delta))/(2*a))
      raiz2 =int((-b - math.sqrt(delta))/(2*a))
      if raiz1>0 and raiz2<0:
         print("As raízes da equação são ",raiz2,"e ",raiz1,".")      
      else:
         print("As raízes da equação são ",raiz1,"e ",raiz2,".")
         
