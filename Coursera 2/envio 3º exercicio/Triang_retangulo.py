from math import sqrt

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        if self.vet[0] > self.vet[1] and self.vet[0] > self.vet[2]:
            hip = self.vet[0]
            cop = self.vet[1]
            cad = self.vet[2]
        elif self.vet[1] > self.vet[0] and self.vet[1] > self.vet[2]:
            hip = self.vet[1]
            cop = self.et[0]
            cad = self.vet[2]
        else:
            hip = self.vet[2]
            cop = self.vet[0]
            cad = self.vet[1]

        if hip == sqrt(self.cop**2 + self.cad**2):
            return True
        else:
            return False
        
'''vet = [0]*3
for i in range(3):
    vet[i] = float(input('Digite um valor: '))'''

'''if retangulo(vet) == True:
    print('É retângulo')
else:
    print('Não é retângulo')'''

'''retangulo(vet)
print(retangulo(vet))'''
ret = Triangulo(1, 3, 5)
print(ret.retangulo())
print('=='*20)
ret1 = Triangulo(3, 4, 5)
print(ret1.retangulo())
