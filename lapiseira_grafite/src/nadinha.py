class Lapiseira:
    def __init__(self, capacidade_maxima):
        self.capacidade_maxima = capacidade_maxima
        self.capacidade_atual = 0

    def inserir_grafite(self, quantidade):
        if self.capacidade_atual + quantidade <= self.capacidade_maxima:
            self.capacidade_atual += quantidade
            print(f'Inserido {quantidade}mm de grafite na lapiseira.')
        else:
            print('A lapiseira está cheia. Não é possível inserir mais grafite.')

    def escrever(self, texto):
        if self.capacidade_atual > 0:
            print(f'Escrevendo: {texto}')
            self.capacidade_atual -= len(texto)
        else:
            print('A lapiseira está sem grafite. Recarregue-a.')

    def recarregar(self):
        self.capacidade_atual = self.capacidade_maxima
        print('Lapiseira recarregada.')


minha_lapiseira = Lapiseira(5)
minha_lapiseira.inserir_grafite(3)
minha_lapiseira.escrever('Programação Orientada a Objetos')
minha_lapiseira.recarregar()
minha_lapiseira.inserir_grafite(10)