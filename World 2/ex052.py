import math
n1 = int(input('Digite um numero :'))
if n1 > 1:
    primo = True
    for i in range (2, n1):
        if n1 % i == 0:
            primo = False
if primo == True:
    print('O numero é primo')
elif primo == False:
    print('O numero não é primo')
else:
    print('Numeros menores ou iguais a 1 não são primos.')