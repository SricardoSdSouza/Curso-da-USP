def encontra_impares(lista):

    # Define a lista que armazenará os números ímpares:
    lis = []
    # Verifica se há elementos na lista:
    if len(lista) > 0:

        # Retira o primeiro elemento da lista:
        numero = lista.pop(0)

        # Verifica se o número é ímpar:
        if numero % 2 != 0:

            # Sim, então adiciona-o à lista de ímpares:
            lis.append(numero)

        # Faz a união do resultado atual com o retorno para o resto da lista:
        lis = lis + encontra_impares(lista)

    # Retorna a lista final:
    return lis

print(encontra_impares([2,4,5,8,1,5]))

import pytest

@pytest.mark.parametrize('entrada, esperado',[
    ([2,4,5,8,1,5],[5,1,5] ),
    ([2,4,6,8,1,12],[1]),
    ([20,40,51,80],[51]),
    ([1,3,5,7,9],[1,3,5,7,9]),
    ])
def testa_encontra_impares(entrada,esperado):
    assert encontra_impares(entrada) == esperado
