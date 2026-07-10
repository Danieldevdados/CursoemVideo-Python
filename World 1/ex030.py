from time import sleep
print('================= PAR OU IMPAR ? ============')
n = int(input('Digite um numero : '))
print('PROCESSANDO.......')
sleep(2)
if n % 2 == 0 :
    print ('O numero é PAR')
else :
    print('O numero é IMPAR')