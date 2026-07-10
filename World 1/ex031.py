from time import sleep
print('========= AGENCIA DE VIAGENS ==============')
dis = float(input('Digite a distancia da viagem : '))
print('CALCULANDO.....')
sleep(0.5)
if dis <= 200 :
    print (' O valor da viagem foi $R {:.2f} '.format(0.50 * dis))
else :
    print('O valor da viagem foi $R {:.2f}'.format(0.45 * dis))