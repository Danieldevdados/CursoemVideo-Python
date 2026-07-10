maior = 0
menor = 0
for c in range(5):
    peso = float(input('Digite seu peso : '))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
            if peso < menor:
                menor = peso
print('O peso maior é {} '.format(maior))
print('O peso menor é  {} '.format(menor))