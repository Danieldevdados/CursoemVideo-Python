from time import sleep
from datetime import date
ano = int(input('Digite o ano ? Coloque 0 para usar o ano atual :'))
print('PROCESSANDO........')
sleep(1)
if ano == 0 :
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano  {} é bissexto'.format(ano))
else:
    print('O ano {} não e bissexto'.format(ano ))