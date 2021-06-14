
print("Vamos calcular as raízes de uma equação de 2º grau")
import math
class Bhaskara:
   def delta (self, a, b, c):
      return b ** 2 - 4 * a * c

   def main(self):
      a_dig=float(input("Digite o coeficiente de a = "))
      b_dig=float(input("Digite o coeficiente de b = "))
      c_dig=float(input("Digite o coeficiente de c = "))
      print(self.calcula_raizes(a_dig,b_dig,c_dig))
      
   def calcula_raizes(self, a, b, c):
      d = self.delta(a, b, c)
      if d == 0:
         raiz1 =(-b + math.sqrt(d))/(2*a)
         return 1, raiz1
      else:
         if d <0:
            return 0
         else:
            raiz1 =(-b + math.sqrt(d))/(2*a)
            raiz2 =(-b - math.sqrt(d))/(2*a)
            return 2, raiz1, raiz2

    
