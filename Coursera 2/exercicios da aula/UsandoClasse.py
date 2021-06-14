def main():
    carro1 = Carro('Brasilia',1968,'Amarela',80)
    carro2 = Carro('Fuscão',1981,'Preto',95)

    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)

class Carro:
    def __init__(self, m, a, c, vm):
        self.modelo = m
        self.ano = a
        self.cor = c
        self.vel = 0
        self.maxV = vm #velocidade máxima

    def imprima(self):
        if self.vel == 0: # parado da para ver o ano
            print('%s %s %d'%(self.modelo, self.cor, self.ano)     )
        elif self.vel < self.maxV:
            print("%s %s indo a %d km/h"%(self.modelo, self.cor, self.vel) )
        else:
            print("%s %s indo muito raaaaapiiiiiidooooo!"%(self.modelo, self.cor) )

    def acelere(self, velocidade):
        self.vel = velocidade
        if self.vel > self.maxV:
            self.vel = self.maxV
        self.imprima()

    def pare(self):
        self.vel = 0
        self.imprima()

main()
