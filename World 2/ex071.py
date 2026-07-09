print('-=' * 12)
print('CAIXA ELETRONICO')
print('-=' * 12)

n = int(input('Digite o valor que você quer sacar : R$ '))
total = n
ced = 100
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break

