from random import choice
from time import sleep

opcoes = ['Pedra','Papel','Tesoura']
computador = choice(opcoes)
jogador = input('Digite o que você vai jogar: ').capitalize()

print('O computador escolheu {}'.format(computador))
print('E o jogador escolheu {}'.format(jogador))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)


if jogador == computador:
    print('EMPATE')
elif (jogador == 'Pedra' and computador == 'Tesoura') or \
     (jogador == 'Papel' and computador == 'Pedra') or \
     (jogador == 'Tesoura' and computador == 'Papel'):
    print('Você ganhou!')
else:
    print('Computador ganhou!')
