#ex086 and 087

matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = soma_coluna = 0

for c in range(3):
    for l in range(3):
        matriz[c][l] = int(input(f'Digite um valor para a posição [{c}, {l}] : '))

print('-=' * 30)
for c in range(3):
    for l in range(3):
        print(f'[{matriz[c][l]:^5}]', end='')
    print()

# soma de todos os pares
for c in range(3):
    for l in range(3):
        if matriz[c][l] % 2 == 0:
            soma += matriz[c][l]
print(f'A soma de todos os valores pares é {soma}')

# soma da terceira coluna
for c in range(3):
    soma_coluna += matriz[c][2]
print(f'A soma de todos os valores da terceira coluna é {soma_coluna}')

# maior valor da segunda linha
maior = max(matriz[1])
print(f'O maior valor da segunda linha é {maior}')
