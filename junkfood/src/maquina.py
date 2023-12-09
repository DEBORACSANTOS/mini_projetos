from src.espiral import Espiral


class Maquina:

    def __init__(self, quantidadeEspirais: int, maximoProdutos: int):
        self.quantidadeEspirais = quantidadeEspirais
        self.MaximoProdutos = maximoProdutos
        self.SaldoCliente = 0
        self.Faturamento = 0
        self.Espirais = [Espiral() for _ in range(quantidadeEspirais)]

    def getFaturamento(self) -> float:
        return self.Faturamento

    def getMaximoProdutos(self) -> int:
        return self.MaximoProdutos

    def getSaldoCliente(self) -> float:
        return self.SaldoCliente

    def getSizeEspirais(self) -> int:
        return self.quantidadeEspirais

    def getEspiral(self, indice: int) -> Espiral:
            if 0 <= indice < len(self.Espirais):
                return self.Espirais[indice]
            return None
    def inserirDinheiro(self, value: float) -> bool:
        if value > 0:
            self.SaldoCliente += value
            return True
        return False

    def receberTroco(self) -> float:
        troco = self.SaldoCliente
        self.SaldoCliente = 0
        return troco

    def alterarEspiral(self, indice: int, nome: str, quantidade: int, preco: float) -> bool:
        if 0 <= indice < self.quantidadeEspirais:
            if quantidade <= self.MaximoProdutos:
                self.Espirais[indice].setNomeDoProduto(nome)
                self.Espirais[indice].setQuantidade(quantidade)
                self.Espirais[indice].setPreco(preco)
                return True
        return False

    def limparEspiral(self, indice: int) -> bool:
        if 0 <= indice < self.quantidadeEspirais:
            espiral = self.getEspiral(indice)
            if espiral is not None:
                espiral.setNomeDoProduto(' - ')
                espiral.setQuantidade(0)
                espiral.setPreco(0)
                return True
        return False

    def vender(self, indice: int) -> bool:
        if 0 <= indice < self.quantidadeEspirais:
            espiral = self.getEspiral(indice)
            if espiral is not None and espiral.getQuantidade() > 0:
                PrecoProduto = espiral.getPreco()
                if self.SaldoCliente >= PrecoProduto:
                    espiral.setQuantidade(espiral.getQuantidade() - 1)
                    if espiral.getQuantidade() == 0:
                        espiral.setNomeDoProduto(' - ')
                        espiral.setPreco(0)
                    self.SaldoCliente -= PrecoProduto
                    self.Faturamento += PrecoProduto
                    return True
        return False