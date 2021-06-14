class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        
        if self.a == self.b == self.c:
           return "equilátero"
        elif self.a != self.b != self.c != self.a:
            return "escaleno"
        else:
           return "isósceles"



'''#t = Triangulo(3, 4, 5)
#t = Triangulo(1, 2, 4)
t = Triangulo(1, 1, 3)
print(t.a)
print(t.b)
print(t.c)
print(t.perimetro())
print(t.tipo_lado())'''
