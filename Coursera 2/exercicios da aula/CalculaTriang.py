import math
import turtle

def q(numero):
  return (numero*numero)
  

# programa principal
a = float(input("Informe o lado a\n"))

b = float(input("Informe o lado b\n"))
c = float(input("Informe o lado c\n"))
if (a < b+c and b < a+c and c < b+a):
  print("Forma triangulo")
else:
  print("Nao forma triangulo")

if ( a==b and b==c) :
  print("Triangulo Equilatero")
elif (a==b or b==c or a==c) :
  print("Isoceles")
else:
  print("Escaleno")

#calcular os angulos
angulo_c = math.acos( (q(a) +q(b) -q(c)) / (2*a*b));
angulo_a = math.acos( (q(b) +q(c) -q(a)) / (2*b*c));
angulo_b = 3.1415 - angulo_a - angulo_c ;
# converter de radianos para graus e de angulo interno para externo
angulo_c = 180- (180 / 3.1415 * angulo_c);
angulo_a = 180 -(180 / 3.1415 * angulo_a);
angulo_b = 180-(180 / 3.1415 * angulo_b);
print("clique na aba result")  
turtle.showturtle()
turtle.penup()
turtle.setpos(-50,0)
turtle.pencolor("blue")
turtle.pendown()
turtle.forward(a)
turtle.left(angulo_c)
turtle.pencolor("green")
turtle.forward(b)
turtle.left(angulo_a)
turtle.pencolor("red")
turtle.forward(c)
