from app.models.frete import Frete


def gerar_frete(peso, distancia, opcao):
    if not isinstance(peso, (int, float)):
        raise TypeError("Peso deve ser numérico")

    if not isinstance(distancia, (int, float)):
        raise TypeError("Distância deve ser numérica")

    if not isinstance(opcao, int):
        raise TypeError("Opção deve ser inteira")

    if peso <= 0:
        raise ValueError("Peso deve ser maior que zero")

    if distancia <= 0:
        raise ValueError("Distância deve ser maior que zero")

    if opcao not in [1, 2, 3]:
        raise ValueError("Opção inválida")

    frete = Frete(distancia, peso)

    if opcao == 1:
        frete.tipo = "Normal"
    elif opcao == 2:
        frete.tipo = "Sedex"
    elif opcao == 3:
        frete.tipo = "Sedex10"

    frete.calcular_preco()

    return f"O valor do frete é {frete.valor:.2f}"
