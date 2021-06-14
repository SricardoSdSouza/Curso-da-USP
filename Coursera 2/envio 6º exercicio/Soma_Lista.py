def soma_lista(lista=list()):
    '''
    :param lista:
    :return:
    >>> soma_lista([1,2,3])
    6
    >>> soma_lista([1,2,3,4])
    10
    >>> soma_lista([1,2,3,4,5,6])
    21
    '''
    if len(lista) >= 1:
        return lista.pop() + soma_lista(lista)
    else:
        return 0


print(soma_lista([1,2,3]))
print('===='*10)
print(soma_lista([4,5,6]))
print('===='*10)
import pytest

@pytest.mark.parametrize('entrada, esperado',[
    ([1,2,3],6 ),
    ([4,5,6],15),
    ([20,40,51,80],191),
    ([1,3,5,7,9],25),
    ([-1,-2,-3,7],1),
    ([1,2,3,4,5,6],21),
    ([1,2,3,4],10),
    ])
def testa_soma_lista(entrada,esperado):
    assert soma_lista(entrada) == esperado
