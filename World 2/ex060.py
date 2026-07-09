from math import factorial
r = 'S'
while r == 'S':
    n = int(input('Digite um numero : '))
    print('{}'.format(factorial(n)))
    r = str(input('Você quer continuar ? S/N ')).upper()
