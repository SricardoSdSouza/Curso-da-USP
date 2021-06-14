import pytest
import Lista_Ordenada    

def testa_lista1():
    assert Lista_Ordenada.ordenada([1,2,3,4,5,6]) == True
    
def testa_lista2():
    assert Lista_Ordenada.ordenada([1,3,2,4,5,6]) == False
    
def testa_lista3():
    assert Lista_Ordenada.ordenada([10,20,30,40,50,60]) == True
    
def testa_lista4():
    assert Lista_Ordenada.ordenada([1,-2,3,4,5,6]) == False
