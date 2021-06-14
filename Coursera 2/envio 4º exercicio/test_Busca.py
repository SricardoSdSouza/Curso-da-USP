import pytest
import Busca


def testa_lista1():
    assert Busca.busca([1,2,3,4,5,6],4) == 3
    
def testa_lista2():
    assert Busca.busca([1,3,2,4,5,6],1) == 0
    
def testa_lista3():
    assert Busca.busca(['a','e','i','o'],'e') == 1
    
def testa_lista4():
    assert Busca.busca([1,-2,3,4,5,6],6) == 5
