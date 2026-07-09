from datetime import date
from time import sleep
ano = int(input('Digite o ano de nascimento : '))
anoatu = date.today().year
idade = anoatu - ano
print('Quem nasceu em {} esta com {} em {}'.format(ano, idade ,anoatu))
print('PROCESSANDO ALISTAMENTO......')
sleep(2)
if idade == 18:
    print('Esta é a hora de você se alistar ')
elif idade > 18 :
    idade = idade - 18
    print('Ja passou {} anos do tempo de você se alistar '.format(idade))
elif idade < 18:
    idade = 18 - idade
    print('Falta ainda {} anos para você se alistar '.format(idade))

