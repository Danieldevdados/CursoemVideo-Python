def aumentar(n, pp=0, f = False):
    p = n * pp / 100
    n += p
    if f == True:
        return f'R${n:.2f}'.replace('.', ',')
    return n


def diminuir(n, pp=0, f = False):
    p = n * pp / 100
    n -= p
    if f == True:
        return f'R${n:.2f}'.replace('.', ',')
    return n


def metade(n, f = False):
    n = n / 2
    if f == True:
        return f'R${n:.2f}'.replace('.', ',')
    return n


def dobro(n, f = False):
    n = n * 2
    if f == True:
        return f'R${n:.2f}'.replace('.', ',')
    return n


def moeda2(n):
    return f'R${n:.2f}'.replace('.', ',')


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


def ex12(n=""):
    if n == "":
        print('"" Nãe é um numero valido!')
        while n == "":
            n = input('Digite o valor: R$')
    elif n.isnumeric() == False:
        print('Apenas numeros ! ')
        while n.isnumeric() == False:
            n = input('Digite o valor: R$')
    n = float(n)
    print('-' * 30)
    print('     RESUMO DO VALOR     ')
    print('-' * 30)
    print(f'Preço Analisado: R${n}')
    print(f'Dobro do preço: R${dobro(n)}')
    print(f'Metade do preço R${metade(n)}')
    print(f'80% de aumento: R${aumentar(n, 80)}')
    print(f'35% de redução: R${diminuir(n, 35)} ')
    print('-' * 30)