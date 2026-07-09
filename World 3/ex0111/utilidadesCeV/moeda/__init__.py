def aumentar(n, pp=0, f = False):
    p = n * pp / 100
    n += p
    if f == True:
        return f'R${n:.2f}'
    return n


def diminuir(n, pp=0, f = False):
    p = n * pp / 100
    n -= p
    if f == True:
        return f'R${n:.2f}'
    return n


def metade(n, f = False):
    n = n / 2
    if f == True:
        return f'R${n:.2f}'
    return n


def dobro(n, f = False):
    n = n * 2
    if f == True:
        return f'R${n:.2f}'
    return n


def moeda2(n):
    return f'R${n:.2f}'