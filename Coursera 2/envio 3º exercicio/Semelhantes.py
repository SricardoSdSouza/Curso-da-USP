from math import sqrt

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tipo_lado(self):
        
        if self.a == self.b == self.c:
           return "equilátero"
        elif self.a != self.b != self.c != self.a:
            return "escaleno"
        else:
           return "isósceles"
        
    def semelhantes(self, Triangulo):
       
        if self.a/Triangulo.a == self.b/Triangulo.b == self.c/Triangulo.c:
            return True
        else:
            return False
        


'''t1 = Triangulo(2, 2, 2)
t2 = Triangulo(4, 4, 4)
print(t1.semelhantes(t2))'''
