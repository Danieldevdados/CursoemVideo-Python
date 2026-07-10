from time import sleep
print('========= MULTAS ===========')
velo = float(input('Digite a velocidade que você estava para descobrir se foi multado : '))
multa = 0
print('PROCESSANDO......')
print('FAZENDO AS CONTAS ......')
sleep(2)
if velo > 80 :
    multa = (velo - 80) * 7
    print('VOCÊ FOI MULTADO NO VALOR DE $R {}'.format(multa))
else :
    print('Você não foi multado')