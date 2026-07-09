print('-=' * 12)
print('LOJãO DO SEU ZÉ')
print('-=' * 12)
total = mais1000 = 0
while True:
    nome = str(input('Nome do produto : '))
    preco = float(input('Digite o preço do produto : R$ '))
    total += preco
    barato = preco
    if barato <= preco:
        barato = preco
    if preco > 1000:
        mais1000 += 1
    r = str(input('Quer continuar ? [S / N ] ')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Quer continuar ? [S / N]')).upper().strip()[0]
    if r == 'N':
        break
print('PAGAMENTO')
print(f'O total da compra ficou R${total:.2f}')
print(f'Temos {mais1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato custa R${barato:.2f}')