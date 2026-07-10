r = 'S'
while r == 'S':
    n1 = int(input('Digite o primeiro termo : '))
    razao = int(input('Digite a razão : '))
    print('Os 10 primeiros termos da razão são ')
    for i in range (0, 10):
        termo = n1 + i * razao
        print('{}'.format(termo))
    r = input('Você quer continuar ? S/N ').upper()