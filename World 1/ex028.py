from random import randint
print('================= PENSADOR DE NUMEROS ====================')
print('Pensando em um numero ....')
r = randint(0, 5)
n= int(input('Digite um numero que eu pensei de 0 a 5  : '))
print('PROCESSANDO ....... ')
print('Você acertou o numero' if n == r else 'Você errou, tente novamente')
print('============ FIM ==============')