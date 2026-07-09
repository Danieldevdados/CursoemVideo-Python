soma = 0
cont = 0
for c in range(0, 500):
    if c % 2 == 1 and c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))