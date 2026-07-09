class Avaliacao:

    def __init__(self, nome, disciplina, nota=0):
        self.nome:str = nome
        self.disciplina:str = disciplina
        self._nota:float = nota


    # Métodos Acessores

    def get_nota(self): # Getter
         return self._nota


    def set_nota(self, valor): # Setter
        if abs(valor) > 10:
            print("Nota invalida")
        else:
            self._nota = valor