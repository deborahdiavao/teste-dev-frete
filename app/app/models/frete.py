class Frete:
    def __init__(self, distancia, peso):
        self._distancia = distancia
        self._peso = peso
        self._tipo = None
        self._valor = 0

    @property
    def valor(self):
        return self._valor

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def calcular_preco(self):
        if self._tipo == "Normal":
            self._valor = self._distancia * self._peso + 5
        elif self._tipo == "Sedex":
            self._valor = self._distancia * self._peso + 10
        elif self._tipo == "Sedex10":
            self._valor = self._distancia * self._peso + 15
