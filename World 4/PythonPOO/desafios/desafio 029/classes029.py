class Diario:

    def __init__(self, senha = "x86@us"):
        self.__mensagens = []
        self.__senha = senha

    def escrever(self,msg):
        self.__mensagens.append(msg)


    def ler(self, senha=None):
        if senha == self.__senha:
            print("DIARIO LIBERADO!")
            for mensagem in self.__mensagens:
                print(f"- {mensagem}")
        else:
            raise PermissionError("Senha invalida! Você não pode ler meu diario!")