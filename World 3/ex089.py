listafull = [[], [], []]  # [nomes, notas, médias]

while True:
    nome = str(input('Nome: ')).strip().lower()
    listafull[0].append(nome)

    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    listafull[1].append([nota1, nota2])  # notas do aluno ficam juntas
    listafull[2].append((nota1 + nota2) / 2)  # média

    r = str(input('Quer continuar ? [S/ N] ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Quer continuar ? [S/ N] ')).strip().upper()[0]
    if r == 'N':
        break

# Menu
r1 = int(input('''\n[ 1 ] BOLETIM COMPLETO
[ 2 ] Nota de um aluno
Escolha: '''))

if r1 == 1:
    print('\nBOLETIM COMPLETO')
    for i in range(len(listafull[0])):
        print(f'{listafull[0][i]:<10} Notas: {listafull[1][i]}  Média: {listafull[2][i]:.1f}')

elif r1 == 2:
    aluno = str(input('Digite o nome do aluno: ')).strip().lower()
    if aluno in listafull[0]:
        idx = listafull[0].index(aluno)
        print(f'\nAluno: {aluno}')
        print(f'Notas: {listafull[1][idx]}')
        print(f'Média: {listafull[2][idx]:.1f}')
    else:
        print('Aluno não encontrado!')
