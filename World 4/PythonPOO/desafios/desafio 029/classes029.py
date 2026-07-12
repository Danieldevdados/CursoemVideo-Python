class Diario:

    def __init__(self, senha = "x86@us"):
        self.__mensagens: list(str) = []
        self.__senha: str = senha.strip()

    def escrever(self,msg):
        self.__mensagens.append(msg)

    @property
    def senha(self):
        raise PermissionError("Ninguem pode ler a senha!")

    @senha.setter
    def senha(self, novasenha, senha):
        if senha == self__senha:
            self.__senha = novasenha
        else:
            raise PermissionError("Senha invalida")

    def ler(self, senha=None):
        if senha == self.__senha:
            print("DIARIO LIBERADO!")
            for mensagem in self.__mensagens:
                print(f"- {mensagem}")
        else:
            raise PermissionError("Senha invalida! Você não pode ler meu diario!")