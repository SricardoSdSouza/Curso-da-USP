import Ordenacao
import pytest
import contaTempos

class TestaOrdenador:

    @pytest.fixture
    def o(self):
        return Ordenacao.Ordenador()

    @pytest.fixture
    def l_quase(self):
        c = contaTempos.ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def l_aleatoria(self):
        c = contaTempos.ContaTempos()
        return c.lista_aleatoria(100)

    def esta_ordenada(self, lis):
        for i in range(len(lis)-1):
            if lis[i] > lis[i+1]:
                return False
        return True

    def test_bolha_curta_aleat(self, o, l_aleatoria):
        o.bolha_curta(l_aleatoria)
        assert self.esta_ordenada(l_aleatoria)

    def test_selecao_direta_aleat(self, o, l_aleatoria):
        o.selecao_direta(l_aleatoria)
        assert self.esta_ordenada(l_aleatoria)

    def test_bolha_curta_quase(self, o, l_quase):
        o.bolha_curta(l_quase)
        assert self.esta_ordenada(l_quase)

    def test_selecao_direta_quase(self, o, l_quase):
        o.selecao_direta(l_quase)
        assert self.esta_ordenada(l_quase)
