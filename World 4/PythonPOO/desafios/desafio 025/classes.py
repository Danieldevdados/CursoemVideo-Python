from abc import ABC , abstractmethod
from rich import print

class Transporte(ABC):

    def __init__(self, distancia):
        self.distancia:float = distancia
        self.frete:float = 0

    @abstractmethod
    def __str__(self):
            pass



class Moto(Transporte):
     fator = 0.5

     def __str__(self):
         self.frete = Moto.fator * self.distancia
         return str(self.frete)


class Caminhao(Transporte):
    fator = 1.2

    def __str__(self):
        if self.distancia >= 50:

            self.frete = Caminhao.fator * self.distancia
            return str(self.frete)
        else:
            return "Raio mínimo de 50 Km"


class Drone(Transporte):
    fator = 9.5

    def __str__(self):
        if self.distancia <= 10:

            self.frete = Drone.fator * self.distancia
            return str(self.frete)
        else:
            return "Raio maximo de 10 Km"