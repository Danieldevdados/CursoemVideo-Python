soma = quantidade = 0
while True:
    n = int(input('Digite um valor [ 999 para parar ]  : '))
    if n != 999:
        quantidade += 1
        soma += n
    if n == 999:
        break
print(f'A soma dos {quantidade} valores foi {soma} !')