class ContatoNotFoundException(Exception):
    pass

class CirculoNotFoundException(Exception):
    pass

class Contato:
    def __init__(self, identificador, email):
        self.identificador = identificador
        self.email = email
        self.favorito = False

class Circulo:
    def __init__(self, identificador, limite_armazenamento):
        self.identificador = identificador
        self.limite_armazenamento = limite_armazenamento
        self.contatos = []

class Sistema:
    def __init__(self):
        self.contatos = {}
        self.circulos = {}

    def adicionar_contato(self, identificador, email):
        if identificador in self.contatos:
            raise ValueError("Identificador já em uso")
        self.contatos[identificador] = Contato(identificador, email)

    def remover_contato(self, identificador):
        if identificador not in self.contatos:
            raise ContatoNotFoundException("Contato não encontrado")
        del self.contatos[identificador]

    def atualizar_email_contato(self, identificador, novo_email):
        if identificador not in self.contatos:
            raise ContatoNotFoundException("Contato não encontrado")
        self.contatos[identificador].email = novo_email

    def buscar_contato(self, identificador):
        if identificador not in self.contatos:
            raise ContatoNotFoundException("Contato não encontrado")
        return self.contatos[identificador]

    def adicionar_favorito(self, identificador):
        if identificador not in self.contatos:
            raise ContatoNotFoundException("Contato não encontrado")
        self.contatos[identificador].favorito = True

    def remover_favorito(self, identificador):
        if identificador not in self.contatos:
            raise ContatoNotFoundException("Contato não encontrado")
        self.contatos[identificador].favorito = False

    def listar_favoritos(self):
        return [contato for contato in self.contatos.values() if contato.favorito]

    def verificar_favorito(self, identificador):
        if identificador not in self.contatos:
            raise ContatoNotFoundException("Contato não encontrado")
        return self.contatos[identificador].favorito

    def adicionar_circulo(self, identificador, limite_armazenamento):
        if identificador in self.circulos:
            raise ValueError("Identificador de círculo já em uso")
        self.circulos[identificador] = Circulo(identificador, limite_armazenamento)

    def remover_circulo(self, identificador):
        if identificador not in self.circulos:
            raise CirculoNotFoundException("Círculo não encontrado")
        del self.circulos[identificador]

    def atualizar_limite_circulo(self, identificador, novo_limite):
        if identificador not in self.circulos:
            raise CirculoNotFoundException("Círculo não encontrado")
        self.circulos[identificador].limite_armazenamento = novo_limite

    def buscar_circulo(self, identificador):
        if identificador not in self.circulos:
            raise CirculoNotFoundException("Círculo não encontrado")
        return self.circulos[identificador]

    def listar_circulos(self):
        return list(self.circulos.values())

    def numero_de_circulos(self):
        return len(self.circulos)

    def adicionar_contato_em_circulo(self, identificador_contato, identificador_circulo):
        if identificador_contato not in self.contatos:
            raise ContatoNotFoundException("Contato não encontrado")
        if identificador_circulo not in self.circulos:
            raise CirculoNotFoundException("Círculo não encontrado")

        circulo = self.circulos[identificador_circulo]
        if len(circulo.contatos) < circulo.limite_armazenamento:
            circulo.contatos.append(self.contatos[identificador_contato])
        else:
            raise ValueError("Limite de armazenamento do círculo atingido")

    def remover_contato_de_circulo(self, identificador_contato, identificador_circulo):
        if identificador_contato not in self.contatos:
            raise ContatoNotFoundException("Contato não encontrado")
        if identificador_circulo not in self.circulos:
            raise CirculoNotFoundException("Círculo não encontrado")

        circulo = self.circulos[identificador_circulo]
        if self.contatos[identificador_contato] in circulo.contatos:
            circulo.contatos.remove(self.contatos[identificador_contato])
        else:
            raise ValueError("Contato não pertence ao círculo")

    def listar_circulos_de_contato(self, identificador_contato):
        if identificador_contato not in self.contatos:
            raise ContatoNotFoundException("Contato não encontrado")
        return [circulo for circulo in self.circulos.values() if self.contatos[identificador_contato] in circulo.contatos]

    def circulos_em_comum(self, identificador_contato1, identificador_contato2):
        if identificador_contato1 not in self.contatos or identificador_contato2 not in self.contatos:
            raise ContatoNotFoundException("Contato não encontrado")

        circulos_contato1 = set(self.listar_circulos_de_contato(identificador_contato1))
        circulos_contato2 = set(self.listar_circulos_de_contato(identificador_contato2))

        circulos_em_comum = circulos_contato1.intersection(circulos_contato2)
        return sorted(list(circulos_em_comum), key=lambda x: x.identificador)

# Exemplo de Uso:
sistema = Sistema()

# Adicionando contatos
sistema.adicionar_contato("contato1", "contato1@example.com")
sistema.adicionar_contato("contato2", "contato2@example.com")

# Adicionando círculos
sistema.adicionar_circulo("circulo1", 2)
sistema.adicionar_circulo("circulo2", 3)

# Adicionando contatos aos círculos
sistema.adicionar_contato_em_circulo("contato1", "circulo1")
sistema.adicionar_contato_em_circulo("contato1", "circulo2")
sistema.adicionar_contato_em_circulo("contato2", "circulo2")

# Removendo contatos de círculos
sistema.remover_contato_de_circulo("contato1", "circulo1")

# Listando círculos de um contato
print(sistema.listar_circulos_de_contato("contato1"))

# Verificando círculos em comum entre dois contatos
print(sistema.circulos_em_comum("contato1", "contato2"))
