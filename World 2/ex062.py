r = 'S'
while r == 'S':
    n1 = int(input('Digite o primeiro termo : '))
    razao = int(input('Digite a razão : '))
    print('Os 10 primeiros termos da razão são ')
    for i in range (0, 10):
        termo = n1 + i * razao
        print('{} - '.format(termo),end='')

    maistermos = int(input('Você quer ver mais quantos termos? '))
    for i in range (10, 10 + maistermos):
        termo = n1 + i * razao
        print('{}'.format(termo))
    r = str(input('Deseja continuar? [S/N] ')).upper()
