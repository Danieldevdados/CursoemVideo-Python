from datetime import date
maior = 0
menor = 0
anoatu= date.today().year
for c in range (0,7):
    anodenascimento = int(input('Digite seu ano de nascimento : '))
    idade = anoatu - anodenascimento
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Existem {} pessoas maiores de idade e {} pessoas menores de idade'.format(maior, menor))
