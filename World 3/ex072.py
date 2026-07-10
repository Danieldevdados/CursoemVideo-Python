extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze' , 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um numero entre 0 e 20 : '))
    while not 0 <= n <= 20:
        print('Tente novamente.. ')
        n = int(input('Digite um numero entre 0 e 20 : '))
    print(f'O numero que você digitou é {extenso[n]}')
    r = str(input('Você quer continuar ? [S / N] ')).upper().strip()[0]
    if r == 'N':
        break
print('Acabou')