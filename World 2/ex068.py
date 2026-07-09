from random import randint
print('-=' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 20)
vitorias = 0
while True:
    njogador = int(input('Diga um valor : '))
    vjogador = str(input('Par ou Ímpar [ P / I ] ? ')).upper().strip()[0]
    while vjogador not in 'PI':
        vjogador = str(input('Par ou Ímpar [ P / I ] ? ')).upper().strip()[0]
    computador = randint(0,10)
    result = njogador + computador
    if vjogador == 'P' and result % 2 == 0:
        print('O jogador venceu')
        print(f'O jogador escolheu {njogador} e o computador {computador} e o resultado {result} é PAR')
        print('VAMOS JOGAR NOVAMENTE....')
        vitorias += 1
    elif vjogador == 'I' and result % 2 == 1:
        print('O jogador venceu')
        print(f'O jogador escolheu {njogador} e o computador {computador} e o resultado {result} é IMPAR')
        print('VAMOS JOGAR NOVAMENTE....')
        vitorias += 1
    else:
        break
print(f'Você perdeu com {vitorias} vitorias ')
