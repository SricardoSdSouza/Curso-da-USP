import Ordenador
import pytest

class TestaOrdenador:

    @pytest.fixture
    def o(self):
        return ordenador.Ordenador()

    @pytest.fixture
    def l_quase(self):
        c = ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def l_aleatoria(self):
        c = ContaTempos()
        return c.lista_aleatoria(100)

    def esta_ordenada(self, lis):
        for i in range(len(lis)-1):
            if lis[i] > lis[i+1]:
                return False
        return True

    def test_bola_curta_aleat(self, o, l_aleat):
        o.bolha_curta(l_aleat)
        assert self.esta_ordenado(l_aleat)
