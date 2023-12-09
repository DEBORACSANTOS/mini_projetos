from pulapula.fonte.crianca import Crianca

class PulaPula:

    def __init__(self, limiteMax):
        self.limeteMax = limiteMax

        self.listaEspera = []
        self.criancaPulando = []

        self.caixa = 0
        self.conta = 0

    def getFilaDeEspera(self):
        return self.listaEspera

    def getCriancasPulando(self):
        return self.criancaPulando

    def getLimiteMax(self):
        return self.limeteMax

    def getCaixa(self):
        return self.caixa

    def getConta(self, nome):
        for crianca in self.criancaPulando:
            if crianca.nome == nome:
                return self.conta

    def entrarNaFila(self, crianca: Crianca):
        if self.listaEspera:
            if self.criancaPulando:
                for crianca in self.criancaPulando:
                    if crianca.nome != crianca.nome:
                        self.listaEspera.append(crianca)
                        return True
                    return False
            else:
                self.listaEspera.append(crianca)
        else:
            self.listaEspera.insert(0, crianca)
            return True


    def entrar(self):
        if len(self.criancaPulando) < self.limeteMax and len(self.listaEspera) > 0:
            crianca = self.listaEspera[0]
            self.listaEspera.pop(0)
            self.criancaPulando.insert(0,crianca)
            self.conta += 2.50
            return True
        else:
            return False


    def sair(self):
        if len(self.criancaPulando) > 0:
            crianca = self.criancaPulando[0]
            self.criancaPulando.pop(0)
            self.listaEspera.append(crianca)
            return True
        return False


    def papaiChegou(self, nome):
        if self.criancaPulando:
            for crianca in self.criancaPulando:
                if crianca.nome == nome:
                    self.caixa += self.conta
                    self.conta = 0
                    return True
        elif self.listaEspera:
            for crianca in self.listaEspera:
                if crianca.nome == nome:
                    self.caixa += self.conta
                    self.conta = 0
                    self.listaEspera.remove(crianca)
                    return True
        return False


    def fechar(self):
        if self.criancaPulando:
            self.criancaPulando.clear()
            self.conta = None
        if self.listaEspera:
            self.listaEspera.clear()
            self.conta = None
        return -1