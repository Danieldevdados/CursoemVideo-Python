from classes import  *
from rich.table import Table
def main():

    distancia = 22
    valores = [Moto(distancia), Caminhao(distancia), Drone(distancia)]

    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distancia")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")
    for c in range(3):
        tabela.add_row(f"{distancia} Km", f"{type(valores[c]).__name__}", f"R${valores[c] }")
    print(tabela)




if __name__ == "__main__":
    main()