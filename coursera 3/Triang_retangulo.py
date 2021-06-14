from math import sqrt

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        
        if self.a > self.b and self.a > self.c:
            hip = self.a
            cop = self.b
            cad = self.c
        elif self.b > self.a and self.b > self.c:
            hip = self.b
            cop = self.a
            cad = self.c
        else:
            hip = self.c
            cop = self.a
            cad = self.b

        if hip == sqrt(cop**2 + cad**2):
            return True
        else:
            return False

'''ret = Triangulo(1, 3, 5)
print(ret.retangulo())
print('=='*20)
ret1 = Triangulo(3, 4, 5)
print(ret1.retangulo())
print('=='*20)
ret2 = Triangulo(4, 2, 3)
print(ret2.retangulo())
print('=='*20)
ret3 = Triangulo(3, 4, 5)
print(ret3.retangulo())'''

