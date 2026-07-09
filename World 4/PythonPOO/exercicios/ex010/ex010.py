class Avaliacao:

    def __init__(self, nome, disciplina, nota=0):
        self.nome:str = nome
        self.disciplina:str = disciplina
        self._nota:float = nota

    @property
    def nota(self): # getter
        return self._nota

    @nota.setter
    def nota(self, valor):
        if abs(valor) > 10:
              print("nota invalida")
        else:
           self._nota = valor