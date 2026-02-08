escola = dict()
escola['nome'] = str(input('Nome: '))
escola['media'] = float(input(f'Media de {escola["nome"]} : '))
if 5<= escola['media'] < 7:
    escola['situacao'] = 'Recuperação'
elif escola['media'] < 5:
    escola['situacao'] = 'Reprovado'
else:
    escola['situacao'] = 'Aprovado'
for k, v in escola.items():
    print(f'{k} é igual a {v}')