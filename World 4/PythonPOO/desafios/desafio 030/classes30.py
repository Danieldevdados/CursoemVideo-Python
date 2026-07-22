# hashlib sha 256
#.encode() para virar bit
#.digest() para armazenar


import hashlib

class Credencial:

    def __init__(self):
        self.__hash = ""



    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self,senha):
        if len(senha) >= 8:
            self.__hash = hashlib.sha256(senha.encode()).hexdigest()
        else:
            raise ValueError("Senha maior que 8 caracteres!")

    def validar(self, chave):
        hash_login = hashlib.sha256(chave.encode()).hexdigest()
        if self.__hash == hash_login:
            print("Senha Valida!")
        else:
            print("Senha invalida")