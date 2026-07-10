from datetime import date
anodenascimento = int(input('Ano de nascimento : '))
anoatu = date.today().year
tempo = anoatu - anodenascimento
print('O atleta tem {} anos .'.format(tempo))
if tempo <= 9 :
    print('MIRIM')
elif  tempo <=14:
    print('INFANTIL')
elif tempo <= 19:
    print('JUNIOR')
else :
    print('MASTER')