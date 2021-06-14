'''class Pato:
  pass

pato = Pato()
patinho = Pato()
if pato == patinho:
  print("Estamos no mesmo endereço!")
else:
  print("Estamos em endereços diferentes!")'''

def main():
    carro1 = Carro('Fusca', 1962, 'azul',80)
    carro2 = Carro('Eco', 1972, 'Verde',95)
    carro3 = Carro('IX35', 2017, 'Preto',110)

    carro1.acelere(40)
    carro2.acelere(50)
    carro3.acelere(60)
    carro1.acelere(80)
    carro1.pare()
    carro3.pare()
    carro2.acelere(100)
    carro3.acelere(110)

class Carro:
    def __init__(self, m, a, c, vm):
        self.modelo = m
        self.ano = a
        self.cor = c
        self.vel = 0
        self.maxV = vm #velocidade maxima
    def imprima(self):
        if self.vel == 0:# parado da para ver o ano
            print("%s %s %d"%(self.modelo, self.cor, self.ano))
        elif self.vel < self.maxV:
            print("%s %s indo a %d Km/h"%(self.modelo, self.cor, self.vel))
        else:
            print("%s %s indo muito raaaaapiiidoooo %d Km/h"%(self.modelo, self.cor, self.vel))

    def acelere(self, velocidade):
        self.vel = velocidade
        if self.vel > self.maxV:
            self.vel = self.maxV
        self.imprima()

    def pare(self):
        self.vel = 0
        self.imprima()
            

main()


