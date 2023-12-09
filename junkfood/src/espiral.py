class Espiral:

    def __init__(self):
        self.nome = ' - '
        self.quantidade = 0
        self.preço = 0

    def getNomeDoProduto(self):
        return self.nome

    def setNomeDoProduto(self, nome: str):
        self.nome = nome

    def getQuantidade(self):
        return self.quantidade

    def setQuantidade(self, quantidade: int):
        self.quantidade = quantidade

    def getPreco(self):
        return self.preço

    def setPreco(self, preço: float):
        self.preço = preço