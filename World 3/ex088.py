from random import sample
from time import sleep

print('-='*20)
print('Mega Sena')
lista = list()
r = int(input('Quantos jogos você quer que eu sorteie ? '))

for c in range(r):
    # gera 6 números únicos entre 1 e 60
    jogo = sorted(sample(range(1, 61), 6))
    lista.append(jogo)

# mostra os jogos
for i, jogo in enumerate(lista, 1):
    print(f'Jogo {i}: {jogo}')
    sleep(0.50)
