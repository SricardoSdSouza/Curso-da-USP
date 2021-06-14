import random
import AlgoritmoOrdenaçãoBubble
import time
class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [0 for x in range(n)]
        for i in range(n):
            #gera numeros inteiros aleatorios entre 0 e 999
            lista[i] = random.randrange(1000)
        return lista

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lsita1[:]

        o = AlgoritmoOrdenaçãoBubble.Ordenador()

        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print(f'Bolha demorou {depois - antes}segundo')

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print(f'selecao direta demorou {depois - antes}segundo')
