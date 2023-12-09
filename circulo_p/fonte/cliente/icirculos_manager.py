from abc import ABC, abstractmethod

from src.cliente.circulo_base import CirculoBase


class ICirculosManager(ABC):

    @abstractmethod
    def createCircle(self, id: str, limite: int) -> bool:
        """
        Adiciona um circulo_p
        Arguments:
            id do circulo_p: Deve ser unico
            limite: define o maximo de contatos que esse circulo_p pode conter
        Returns:
            true caso o contato seja adicionado, false se ja existir um circulo_p com o mesmo id
        """
        pass


    @abstractmethod
    def updateCircle(self, circulo: CirculoBase) -> bool:
        """
        Atualiza o limite do circulo_p
        Arguments:
            circulo: com o mesmo identifador e novo limite
        Returns:
            true caso o circulo_p seja atualizado, false se o circulo_p com nao existir
        """

        pass

    @abstractmethod
    def getCircle(self, idCirculo: int) -> CirculoBase:
        """
        Retorna um circulo_p
        Arguments:
            idCirculo: id do circulo_p a ser recuperado
        Returns:
            circulo_p caso ele exista, None se nenhum circulo_p com o id informado for encontrado
        """
        pass

    @abstractmethod
    def getAllCircles(self) -> list:
        """
        Retorna a lista dos circulos ordenados pelo nome

        Returns:
            a lista dos circulos ordenados pelo nome

        """
        pass

    @abstractmethod
    def removeCircle(self, idCirculo: str) -> bool:
        """
        Remove um circulo_p
        Arguments:
            idCirculo: identificador do circulo_p a ser removido
        Returns:
            true caso o circulo_p seja removido, false se o circulo_p nao existir
        """
        pass

    @abstractmethod
    def getNumberOfCircles(self) -> int:
        """
        Returns:
            o numero de circulos cadastrados
        """
        pass