from rich import inspect

class ContaBancaria:
    """
    Cria uma Conta Bancaria
    """

    def __init__(self, id, n, s = 0):
        self._nome = n # protegido (#)
        self.id = id # publico ( + )
        self.__saldo = s # privado ( - )

    def __str__(self):
        return f"A conta {self.id} de {self._nome} contem R${self.__saldo:.2f} de __saldo."

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Deposito de R${valor} feito totalizando : R${self.__saldo}")

    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print("O saque é maior doque o valor disponivel!")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor} feito restando: R${self.__saldo}")

