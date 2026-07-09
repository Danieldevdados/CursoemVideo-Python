from random import randint
from time import sleep

números = list()

def sorteia():
    print('-='*20)
    print('Sorteando 5 valores : ',end='')
    for c in range(5):
        n = randint(1, 10)
        números.append(n)
        print(f'{n} ',end='')
        sleep(0.5)
    print('PRONTO!')


def somapar():
    s = 0
    for c in range(len(números)):
        if números[c] % 2 == 0:
            s += números[c]
    print(f'Somando os valores pares de {números}, temos {s}')



sorteia()
somapar()