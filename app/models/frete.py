
class Frete:
    def __init__(self, peso: float, distancia: float):
        self.peso = peso
        self.distancia = distancia

    def calcular(self) -> float:
        valor_base = 5.0
        valor_por_kg = 2.0
        valor_por_km = 0.5

        return valor_base + (self.peso * valor_por_kg) + (self.distancia * valor_por_km)
