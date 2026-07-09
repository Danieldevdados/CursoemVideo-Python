from time import sleep
a = int(input('Digite um numero : '))
b = int(input('Digite outro numero : '))
c = int(input('Digite mais um numero : '))
print('Processando..........')
sleep(3)
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor é {} e o maior é {}'.format(menor , maior ))