print("Vamos calcular as raízes de uma equação de 2º grau")
"importando biblioteca de matematica"
import math
"atribuindo valor as variaveis solicitando pelo teclado"
a=float(input("Digite o coeficiente de a = "))
b=float(input("Digite o coeficiente de b = "))
c=float(input("Digite o coeficiente de c = "))

"calculando do delta = b**2 -4 * a * c"
delta=b**2-4*a*c
"calculando as raizes"
raiz1 =float(-b + math.sqrt(delta))/(2*a)
raiz2 =float(-b - math.sqrt(delta))/(2*a)

if delta <0:
   print("Esta equação não tem raizes reais.")

if delta ==0:
        print("Existe somente uma raiz para esta equação.")

if raiz1 <0:
        print("O valor de X1 será negativo =",raiz1)
if raiz1 >0:
        print("O valor de x1 é = ",raiz1)
if raiz2 >0:
        print(" 0 valor de x2 = ",raiz2)
if raiz2 <0:
        print("O valor de X2 será negativo = ",raiz2)
else:
    print("O valor de x1 e x2 = ",raiz1,raiz2)
        
print("O valor de Delta é =",delta)
print("A raiz de Delta = ",math.sqrt(delta))     
print("O resultado final")
print("As raizes são %.2f e %.2f"%(raiz1,raiz2))
