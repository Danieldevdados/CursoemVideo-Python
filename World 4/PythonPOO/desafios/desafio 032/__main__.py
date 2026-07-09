from classes32 import *
from rich import inspect

def main():
    cc = ContaBancaria(111, "Daniel", 1000)
    cc.depositar(1000)
    cc.sacar(1000)
    print(inspect(cc, private=True))

if __name__ == "__main__":
    main()