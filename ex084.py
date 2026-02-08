dados = list()
informacoes = list()
pessoas = 0
while True:
    dados.append(str(input('Nome: ')))
    pessoas += 1
    dados.append(float(input('Peso: ')))
    informacoes.append(dados[:])
    dados.clear()
    r = str(input('Quer continuar? [S/ N]')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/ N]')).strip().upper()[0]
    if r == 'N':
        break
print('-='*20)
print(f'{informacoes}')
print(f'Teve {pessoas} pessoas cadastradas !')
pesos = list()
for p in range(len(informacoes)):
    pesos.append(informacoes[:][p][1])
maior = max(pesos)
menor = min(pesos)
print(f'O maior peso foi {maior} de ', end='')
for p in informacoes:
    if p[1] == maior:
        print(f' {p[0] }',end='')
print()
print(f'O menor peso foi {menor}', end='')
for p in informacoes:
    if p[1] == menor:
        print(f' {p[0] }',end='')