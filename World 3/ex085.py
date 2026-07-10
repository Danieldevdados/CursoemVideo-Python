lista = [[], []]
for p in range(7):
    valor = (int(input(f'Digite o {p+1}.0 valor: ')))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
     lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Pares : {lista[0]}')
print(f'Impares : {lista[1]}')