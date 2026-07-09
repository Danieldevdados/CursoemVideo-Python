class Termostato:

    def __init__(self):
        self.__temperatura = 24


    @property
    def ftemperatura(self):
        return f"{self.__temperatura} °C"

    @ftemperatura.setter
    def temperatura(self,valor):
        if valor < 16:
            self.__temperatura = 16
        elif valor > 30:
            self.__temperatura = 30
        else:
            decimal = valor - int(valor)
            if decimal == 0 or decimal == 0.5:
                self.__temperatura = valor
            else:
                raise ValueError(f"temperatura de {valor} °C invalida")