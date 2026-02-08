from random import randint
from time import sleep


números = list()

def maior():
    print('-=' * 20)
    print('Analisando os valores passados...')
    for c in range(5):
        n = randint(1,10)
        números.append(n)
        print(f'{n} ', end='')
        sleep(0.5)
    print(f'Foram passados {len(números)} valores, e o maior é o {max(números)}')


maior()
