from ex009 import *

def main():
    av = Avaliacao("Daniel", "Matematica", 7.5)
    print(av.get_nota())
    av.set_nota(-0)
    print(av.get_nota())


if __name__ == "__main__":
    main()