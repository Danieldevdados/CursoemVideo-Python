from abc import ABC, abstractmethod
from rich import print

class Personagem(ABC):

    def __init__(self, nome, vida):
        self.nome:str = nome
        self.vida:float = vida
        self.golpes = []

    def atacar(self, alvo, forca):
        pass

    def receber_dano(self, dano):
        pass

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome,vida)
        self.nome: str = nome
        self.vida: float = vida


    def curar(self):
        pass


class Mago(Personagem):

    def __init(self, nome, vida):
        super().__init__(nome, vida)
        self.nome: str = nome
        self.vida: float = vida


    def curar(self):
        pass

