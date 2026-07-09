soma = 0
for c in range (0 , 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        soma += n
print('A soma dos pares é {} '.format(soma))