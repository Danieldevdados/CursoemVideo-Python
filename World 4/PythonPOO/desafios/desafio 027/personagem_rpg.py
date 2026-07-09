import random
from abc import ABC, abstractmethod
from rich import print

class Personagem(ABC):

    def __init__(self, nome, vida):
        self._nome:str = nome # (#)
        self._vida:float = vida # (#)
        self._golpes = [] # (#)

    def atacar(self, alvo, forca=1000):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self._golpes[random.randint(0, (len(self._golpes) - 1))]
            print(f"{self.nome} atacou {alvo.nome} com um {golpe}")
            alvo.receber_dano(forca)
        else:
            print("Não sera possivel realizar o golpe")

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        if self.vida <= 0:
            print(f"O {self.nome} ja esta [red]incapacitado[/]")
        else:
            self.vida -= fator
            if self.vida > 0:
                print(f"{self.nome} recebeu {fator} de dano e agora esta com {self.vida} de vida")
            else:
                print(f"{self.nome} [red]morreu[/]!")

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome,vida)
        self.vida_inicial = vida
        self.golpes = ["Voadora", "Corte Perfurador", "Chute dos Deuses"]


    def curar(self):
        if self.vida == 0:
            print("Não se pode curar um personagem morto")
        else:
            cura = random.randint(0, self.vida_inicial)
            self.vida += cura
            print(f"{self.nome} se curou com uma atadura medieval e recebeu {cura} de cura!")


class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.vida_inicial = vida
        self.golpes = ["Bola de Fogo", "Expansão de dominio", "Alackazam!"]

    def curar(self):
        if self.vida == 0:
            print("Não se pode curar um personagem morto!")
        else:
            cura = random.randint(0, self.vida_inicial)
            self.vida += cura
            print(f"{self.nome} se curou com uma ajuda de sua alquimia  e recebeu {cura} de cura!")

