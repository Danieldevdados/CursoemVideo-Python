n1 = quant = soma = 0
while n1 != 999:
    n1 = int(input('Digite um numero [999 para parar ]  : '))
    quant += 1
    if n1 != 999:
        soma += n1
print('A quantidade de numeros digitados foi {}'.format(quant))
print('A soma de todos os numeros digitados desconsiderando o ultimo foi : {}'.format(soma))
