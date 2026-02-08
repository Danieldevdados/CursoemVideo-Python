soma_idades = 0
mulheres = 0
maioridadehomen = 0
nomehomen = ''
for c in range(4):
    nome = str(input('Digite seu nome : '))
    idade = int(input('Digite sua idade : '))
    sexo = str(input('Digite seu sexo [M/F] : ')).strip().upper()
    soma_idades += idade
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if sexo == 'M':
        if idade > maioridadehomen:
            maioridadehomen = idade
            nomehomen = nome

media = soma_idades / 4
print('A media entre as idades é {}'.format(media))
print('Temos {} mulheres com menos de 20 anos'.format(mulheres))
print('O homen mais velho tem {} anos e seu nome é {}'.format(maioridadehomen, nomehomen))