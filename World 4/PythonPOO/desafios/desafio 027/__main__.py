from personagem_rpg import *


def main():

    p1 = Guerreiro("Pikachu", 1000)
    p2 = Mago("Alask", 120)
    p1.atacar(p2, 50)
    p2.curar()
    p2.atacar(p1)

if __name__ == "__main__":
    main()