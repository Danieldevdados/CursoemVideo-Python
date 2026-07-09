n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

menu = 0
while menu != 5:
    print(''' 
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair
''')
    menu = int(input('Digite a sua opção: '))

    if menu == 1:
        print(f'A soma é {n1 + n2}')

    elif menu == 2:
        print(f'A multiplicação é {n1 * n2}')

    elif menu == 3:
        maior = n1 if n1 > n2 else n2
        print(f'O maior é {maior}')

    elif menu == 4:
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite outro novo número: '))

    elif menu == 5:
        print('Finalizando...')

    else:
        print('Opção inválida! Tente novamente.')

print('Programa encerrado!')
