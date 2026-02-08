from time import sleep
print('========== AUMENTO DE SALARIO ==============')
sl = float(input('Digite o seu salario: '))
print('PROCESSANDO SEU SALARIO.........')
sleep(10)
if sl >= 1250:
    au = sl * 0.10
    nv = sl + au
    print(' O novo salario é {}'.format(nv))
else:
    au = sl * 0.15
    nv = sl + au
    print('O novo salario sera {}'.format(nv))