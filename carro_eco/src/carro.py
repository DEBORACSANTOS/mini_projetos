class Carro:

    def __init__(self):
        self.combustivel = 0
        self.passageiros = 0
        self.quilometragem = 0

    def getPassageiros(self):
        return self.passageiros

    def getCombustivel(self):
        return self.combustivel

    def getQuilometragem(self):
        return self.quilometragem

    def embarcar(self):
        if self.passageiros < 2:
            self.passageiros += 1
            return True
        return False


    def desembarcar(self):
        if self.passageiros > 0:
            self.passageiros -= 1
            return True
        return False

    def dirigir(self, distancia):
        if self.passageiros > 0 and self.combustivel > 0:
            if distancia <= self.combustivel:
                self.quilometragem += distancia
                self.combustivel -= distancia
                return True
            else:
                self.quilometragem += self.combustivel
                self.combustivel = 0
                return False

    def abastecer(self, quantidade):
        if quantidade > 0:
            if self.combustivel + quantidade <= 100:
                self.combustivel += quantidade
            else:
                self.combustivel = 100
            return True
        else:
            return False

    def __str__(self):
        return f'passageiros: {self.passageiros}, combustível: {self.combustivel} litros, quilometragem:{self.quilometragem}km'


