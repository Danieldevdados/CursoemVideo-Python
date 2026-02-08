from random import randint
from time import sleep
from operator import itemgetter
ranking = list()
dados = dict()
print('Valores sorteados: ')
for c in range(4):
    dados[f'jogador{c+1}'] = randint(1, 6)
    print(f'Jogador {c+1} jogou {dados[f"jogador{c+1}"]}')
    sleep(1)
ranking = sorted(dados.items, key=itemgetter(1), reverse=True)
print('-=' * 20)
print('RANKING')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar : {v[0]} com {v[1]}')
    sleep(1)
