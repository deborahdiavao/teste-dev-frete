import pytest
from app.main import gerar_frete


class TestFrete:
    @pytest.mark.parametrize(
        "peso, distancia, opcao, tipo, valor_esperado",
        [
            (2.0, 500, 1, "Normal", 1005.00),
            (2.0, 500, 2, "Sedex", 1010.00),
            (3.4, 500, 3, "Sedex10", 1715.00),
        ],
        ids=["Normal", "Sedex", "Sedex10"],
    )
    def test_gerar_frete_opcoes_validas(
        self, peso, distancia, opcao, tipo, valor_esperado
    ):
        resultado = gerar_frete(peso, distancia, opcao)
        assert resultado == f"O valor do frete é {valor_esperado:.2f}"

    def test_input_peso_invalido(self):
        with pytest.raises(ValueError):
            gerar_frete(-3, 500, 3)

    def test_input_opcao_invalida(self):
        with pytest.raises(ValueError):
            gerar_frete(4, 500, 0)

    def test_input_distancia_invalida(self):
        with pytest.raises(ValueError):
            gerar_frete(4.2, 0, 3)

    def test_gerar_frete_entrada_nao_numerica(self):
        with pytest.raises(TypeError):
            gerar_frete("abc", 500, 1)

    def test_gerar_frete_entrada_nula(self):
        with pytest.raises(TypeError):
            gerar_frete(None, 500, 1)
