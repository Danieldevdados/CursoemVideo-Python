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


def resumo(n):
    print('-'*30)
    print('     RESUMO DO VALOR     ')
    print('-'*30)
    print(f'Preço Analisado: R${n}')
    print(f'Dobro do preço: R${dobro(n)}')
    print(f'Metade do preço R${metade(n)}')
    print(f'80% de aumento: R${aumentar(n, 80)}')
    print(f'35% de redução: R${diminuir(n, 35)} ')
    print('-'*30)


def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO: \"{entrada}\" é um preço invalido!')
        else:
            valido = True
            return float(entrada)