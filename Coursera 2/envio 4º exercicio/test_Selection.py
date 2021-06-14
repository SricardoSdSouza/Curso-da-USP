import pytest
import SelectionSort    
# ESTA COM ERRO NÃO CONSEGUI FAZER O TESTE RODAR
    
def testa_lista1():
    assert SelectionSort.ordena([1,2,3,4,5,6]) == (1,2,3,4,5,6)
    
def testa_lista2(a,b,c,d,f,g):
    assert SelectionSort.ordena([1,6,2,4,7,3]) == (1,2,3,4,6,7)
    
def testa_lista3(a,b,c,d,f,g):
    assert SelectionSort.ordena([10,30,20,60,50,40]) == (10,20,30,40,50,60)
    
def testa_lista4(a,b,c,d,f,g):
    assert SelectionSort.ordena([1,-2,3,4,5,6]) == (-2,1,3,4,5,6)
