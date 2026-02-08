v = []
quant = num5 = 0
while True:
    v.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar [S/ N] ? ')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Quer continuar [S/ N] ? ')).upper().strip()[0]
    if r == 'N':
        break
print(f'Foram digitados {len(v)} numeros ')
print(f'Lista ordenada de forma decrescente : {sorted(v , reverse=True)}')
for i, n in enumerate(v):
    if v == 5:
        num5 += 1
if num5 > 0:
    print(f'O valor 5 foi digitado em {num5} vezes')
elif num5 == 0:
    print('O numero 5 não foi digitado')