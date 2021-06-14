import Bhaskara
import pytest

class TestBhaskara:
    
    @pytest.fixture  #usando este comando fixa uma linha no caso b=Bhaskara.Bhaskara()
    def b(self):
       b = Bhaskara.Bhaskara() 
    def testa_uma_raiz(self, b):
       # b = Bhaskara.Bhaskara()
        assert b.calcula_raizes(1, 0, 0 ) == (1,0)
        
    def testa_duas_raiz(self, b):
        #b = Bhaskara.Bhaskara()
        assert b.calcula_raizes(1, -5, 6 ) == (2, 3, 2)
        
    def testa_zero_raiz(self, b):
       # b = Bhaskara.Bhaskara()
        assert b.calcula_raizes(10, 10, 10 ) == (0)
        
    def testa_raiz_negativa(self, b):
       # b = Bhaskara.Bhaskara()
        assert b.calcula_raizes(10, 20, 10 ) == (1,-1)
