mais18 = homens = mulheres = 0
while True:
    print('-=' * 20)
    print('CADASTRAR PESSOAS')
    print('-=' * 20)
    idade = int(input('Idade : '))
    sexo = str(input('Sexo [M / F] ? ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [M / F] ? ')).upper().strip()[0]
    r = str(input('Quer continuar ? [ S / N ] ')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Quer continuar ? [S / N ]')).upper().strip()[0]
    if idade >= 18:
        mais18 += 1
    elif sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres += 1
    if r == 'N':
        break

print(f'Pessoas maiores de 18: {mais18}')
print(f'Homens cadastrados:  {homens}')
print(f'Mulheres com menos de 20 anos:  {mulheres}')