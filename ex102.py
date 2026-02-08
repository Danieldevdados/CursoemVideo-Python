def Fatorial(n, show=False):
    """
    Calcula o fatorial de um numero
    :param n: Numero a ser calculado
    :param show: Mostrar calculo ou não
    :return: Fatorial de um numero
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

#Programa Principal
print(Fatorial(5, show=False))