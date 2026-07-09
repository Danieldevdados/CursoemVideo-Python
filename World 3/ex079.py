valores = list()
while True:
    n = int(input('Digite um valor'))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado')
    r = str(input('Quer continuar ? [S / N ] ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Quer continuar ? [S / N ] ')).strip().upper()[0]
    if r == 'N':
        break
print(f'Voce adicionou os valores {valores.sort()}')