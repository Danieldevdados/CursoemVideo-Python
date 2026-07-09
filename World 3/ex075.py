while True:
    num = (int(input('Digite um numero : ' )),
            int(input('Digite outro numero : ')),
            int(input('Digite mais um numero : ')),
            int(input('Digite o ultimo numero : ')))
    print(f'Você digitou os valores {num}')
    print(f'O numero 9 apareceu {num.count(9)} vezes ')
    if 3 in num:
        print(f'O numero 3 apareceu primeiro na posição : {num.index(3)+1}')
    else:
        print('O valor 3 não foi digitado')
    print('Os valores pares foram ')
    for n in num:
        if n % 2 == 0:
            print(f'{n}, ', end='')
    r = str(input(' \n Você quer continuar ? [S / N] ')).upper().strip()[0]
    if r == 'N':
        break
print('ACABOU')