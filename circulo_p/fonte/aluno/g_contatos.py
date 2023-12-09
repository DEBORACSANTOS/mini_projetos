from .cliente.circulo_base import CirculoBase
from .cliente.contato_base import ContatoBase
from .cliente.icirculo_operacoes_manager import ICirculoOperationsManager
from .cliente.icirculos_manager import ICirculosManager
from .cliente.icontatos_manager import IContatosManager


class GContatos(IContatosManager, ICirculosManager, ICirculoOperationsManager):


    def __init__(self):
        self.contatos = []
        self.circulos = []


    def createContact(self, id: str, email: str) -> bool:
        if not any(c.id == id for c in self.contatos):
            contato = GContatos(id, email)
            self.contatos.append(contato)
            return True
        else:
            return False

    def getAllContacts(self) -> list:
        return self.contatos

    def updateContact(self, contato: ContatoBase) -> bool:
        return False

    def removeContact(self, id: str) -> bool:
        contato = next((c for c in self.contatos if c.id == id ), None)
        if contato:
            self.contatos.remove(contato)
            return True
        else:
            return False

    def getContact(self, id: str) -> ContatoBase:
        return self.contatos[id]

    def getNumberOfContacts(self) -> int:
        return 0

    def favoriteContact(self, idContato: str) -> bool:
        return False

    def unfavoriteContact(self, idContato: str) -> bool:
        return False

    def isFavorited(self, id: str) -> bool:
        return False

    def getFavorited(self) -> list:
        return None

    def createCircle(self, id: str, limite: int) -> bool:
        return False

    def updateCircle(self, circulo: CirculoBase) -> bool:
        return False

    def getCircle(self, idCirculo: str) -> CirculoBase:
        return None

    def getAllCircles(self) -> list:
        return None

    def removeCircle(self, idCirculo: str) -> bool:
        return False

    def getNumberOfCircles(self) -> int:
        return 0

    def tie(self, idContato: str, idCirculo: str) -> bool:
        return False

    def untie(self, idContato: str, idCirculo: str) -> bool:
        return False

    def getContacts(self, id: str) -> list:
        return None

    def getCircles(self, id: str) -> list:
        return None

    def getCommomCircle(self, idContato1: str, idContato2: str) -> list:
        return None