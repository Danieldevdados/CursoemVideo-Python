def ficha(n=0,g=0):
    """

    :param n: Nome do jogador
    :param g: Quantidade de gols do jogador
    :return:
    """

    if len(n) == 0 and len(g) == 0:
        n = '<desconhecido>'
        g = '0'
    elif len(n) == 0:
        n = '<desconhecido>'
    elif len(g) == 0:
        g == int(g)
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')




print('-='*20)
nome = input('Nome do jogador: ')
gols = input(f'Quantos gols {nome} fez ? ')
ficha(nome, gols)
help(ficha)