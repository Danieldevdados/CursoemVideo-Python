r = 'S'
quant = media = maior = menor = soma = 0
while r == 'S':
    n = int(input('Digite um valor : '))
    r = str(input('Você quer continuar ? S/N ')).upper()
    quant += 1
    soma += n
    if n > maior:
        maior = n
    if n < maior:
        menor = n
media = soma / quant
print('A media entre todos os valores foi {}'.format(media))
print('O maior numero foi {}'.format(maior))
print('O menor numero foi {}'.format(menor))
