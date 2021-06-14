import random
import Ordenacao
import time
class ContaTempos:
    #refatoração da função lista_aleatoria
    #def lista_aleatoria(self, n):
        #lista = [0 for x in range(n)]
        #for i in range(n):
            #gera numeros inteiros aleatorios entre 0 e 999
            #lista[i] = random.randrange(1000)
        #return lista
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]

        o = Ordenacao.Ordenador()

        print('Comparando com listas aleatorias')
        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print(f'Bolha curta demorou {depois - antes}segundo')

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print(f'selecao direta demorou {depois - antes}segundo')

        print('\nComparando com listas quase ordenadas')
        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]
        
        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print(f'Bolha curta demorou {depois - antes}segundo')

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print(f'selecao direta demorou {depois - antes}segundo')
