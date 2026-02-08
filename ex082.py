lista = []
impares = []
pares = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    r = str(input('Quer continuar ? [S / N ] ')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Quer continuar ? [S / N ] ')).upper().strip()[0]
    if r == 'N':
        break
print(f'Você digitou os valores {lista}')
for i,v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'VOcê digitou os valores pares {pares}')
print(f'Você digitou os valores impares {impares}')