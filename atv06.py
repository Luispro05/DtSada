class Veiculo:
    def __init__(self, combustivel, numero_passageiros, eficiencia, maximo_de_combustivel):
        self.combustivel = combustivel
        self.numero_passageiros = numero_passageiros
        self.eficiencia = eficiencia #distancia em Km consumindo 1 litro de combustivel
        self.maximo_de_combustivel = maximo_de_combustivel
        self.quantidade_no_tanque = 0
    def mede_consumo(self, distancia):
        consumo = distancia/self.eficiencia
        return consumo
    def abastecer(self, quantidade_abastecendo):
        if(self.quantidade_no_tanque + quantidade_abastecendo <= self.maximo_de_combustivel):
            self.quantidade_no_tanque += quantidade_abastecendo
        else:
            self.quantidade_no_tanque = self.maximo_de_combustivel
    def chega_la(self, distancia):
        maxima_distancia = self.quantidade_no_tanque * self.eficiencia
        if (distancia <= maxima_distancia):
            return True
        else:
            return False