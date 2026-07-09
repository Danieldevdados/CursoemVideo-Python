n1= float(input('Digite a primeira nota : '))
n2 = float(input('Digite a segunda nota : '))
media = (n1 + n2) / 2
if media < 5:
    print('Você foi reprovado, estude mais ! ')
elif 5 <= media <= 6.9:
    print('Recuperação ')
else:
    print('Aprovado')
