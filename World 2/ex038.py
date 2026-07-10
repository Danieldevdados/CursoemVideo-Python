n1 = int(input('Digite o primeiro  numero : '))
n2 = int(input('Digite o segundo  numero : '))
if n1 > n2:
    maior = n1
    print('O maior numero é o primeiro : {}'.format(maior))
elif n2 > n1:
    maior = n2
    print('O maior numero é o segundo : {}'.format(maior))
elif n1 == n2 :
    print('Não existe valor maior os dois são iguais')