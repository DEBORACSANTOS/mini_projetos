class Tamagotchi:

    def __init__(self, energiaMax:int, saciedadeMax:int, limpezaMax:int, idadeMax:int ):
        self.energiaMax = energiaMax
        self.saciedadeMax = saciedadeMax
        self.limpezaMax = limpezaMax
        self.idadeMax = idadeMax

        self.energia_atual = energiaMax
        self.saciedade_atual = saciedadeMax
        self.limpeza_atual = limpezaMax

        self.idade_atual = 0
        self.diamantes = 0
        self.estar_vivo = True


    def getEnergiaMax(self):
        return self.energiaMax

    def getSaciedadeMax(self):
        return self.saciedadeMax

    def getLimpezaMax(self):
        return self.limpezaMax

    def getIdadeMax(self):
        return self.idadeMax

    def getEnergiaAtual(self):
        return self.energia_atual

    def getSaciedadeAtual(self):
        return self.saciedade_atual

    def getLimpezaAtual(self):
        return self.limpeza_atual

    def getIdadeAtual(self):
        return self.idade_atual

    def getDiamantes(self):
        return self.diamantes

    def getEstaVivo(self):
        if self.energia_atual > 0 and self.limpeza_atual > 0 and self.saciedade_atual > 0 and self.idade_atual != self.idadeMax:
            self.estar_vivo = True
            return True
        else:
            self.estar_vivo = False
            return False

    def brincar(self):
        if self.getEstaVivo() == True:
            self.energia_atual -= 2
            self.saciedade_atual -= 1
            self.limpeza_atual -= 3
            self.diamantes += 1
            if self.energia_atual < 0:
                self.energia_atual = 0
            if self.saciedade_atual < 0:
                self.saciedade_atual = 0
            if self.limpeza_atual < 0:
                self.limpeza_atual = 0
            if self.idade_atual + 1 <= self.idadeMax:
                self.idade_atual += 1
                return True
        else:
            return False

    def comer(self):
        if self.getEstaVivo() == True:
            self.energia_atual -= 1
            self.limpeza_atual -= 2
            if self.energia_atual < 0:
                self.energia_atual = 0
            if self.limpeza_atual < 0:
                self.limpeza_atual = 0
            if self.idade_atual + 1 <= self.idadeMax:
                self.idade_atual += 1
            if self.saciedade_atual + 4 <= self.saciedadeMax:
                self.saciedade_atual += 4
            else:
                self.saciedade_atual = self.saciedadeMax
                return True
        else:
            return False


    def dormir(self):
        if self.getEstaVivo() == True:
            if self.energiaMax - self.energia_atual >= 5:
                self.idade_atual += self.energiaMax - self.energia_atual
                if self.idade_atual > self.idadeMax:
                    self.idade_atual = self.idadeMax
                self.energia_atual = self.energiaMax
                self.saciedade_atual -= 2
                return True
            else:
                return False
        else:
            return False


    def banhar(self):
        if self.getEstaVivo() == True:
            self.energia_atual -= 3
            self.saciedade_atual -= 1
            self.limpeza_atual = self.limpezaMax
            if self.idade_atual + 2 <= self.idadeMax:
                self.idade_atual += 2
            else:
                self.idade_atual = self.idadeMax
            return True
        else:
            return False
