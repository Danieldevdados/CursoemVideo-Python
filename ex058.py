from random import randint
computador = randint(0, 10)
jogador = 0
tentativas = 1
print('Pensarei em um numero de 0 a 10 tente adivinhar !')
while jogador != computador:
    jogador = int(input('Qual seu palpite ?  '))
    if jogador > computador :
        print('Menos... tente novamente ')
        tentativas += 1
    if jogador < computador:
        print('Mais... tente novamente ')
        tentativas += 1
print('Você acertou parabens...')
print('O jogador so acertou o numero depois de {} tentativas'.format(tentativas))