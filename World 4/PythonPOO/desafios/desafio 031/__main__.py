from classes31 import *
from rich import inspect


def main():
    r = Retangulo()
    r.base = 4
    r.altura = 8
    print(inspect(r,private=True))

if __name__ == "__main__":
    main()