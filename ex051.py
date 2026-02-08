n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão : '))
print('Os 10 primeiros termos da razão PA são : ')
for i in range (0, 10):
    termo = n1 + i * r
    print('{}'.format(termo, end='-'))