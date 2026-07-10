geral = list()
total = 0
while True:
    nome = str(input('Nome: '))
    sexo = str(input('Sexo : [M / F] ')).upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo : [M / F] ')).upper()[0]
    idade = int(input('Idade : '))
    geral.append({
    'nome': nome,
     'sexo': sexo,
        'idade': idade,
    })
    resp = str(input('Quer continuar ? [S/ N ]')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 20)
print(f'O grupo tem {len(geral)} pessoas')
for i in range(len(geral)):
    total += geral[i]['idade']
media = total / len(geral)
print(f'A media das idades é {media}')
for s in range(len(geral)):
    if geral[s]['sexo'] == 'F':
        print(f'As mulheres cadastradas foram {geral[s]["nome"]}')
print('Lista de pessoas com idade acima da media')
for m in range(len(geral)):
    if geral[m]["idade"] > media:
        print(f'{geral[m]}')