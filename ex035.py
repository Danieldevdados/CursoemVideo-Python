print('-=' * 20)
print('ANALISADOR DE TRIANGULOS')
print('-=' * 20)
a = int(input('Digite a primeiro segmento : '))
b = int(input('Digite a segundo segmento : '))
c = int(input('Digite a terceiro segmento : '))
if a < b + c and b < a + c and c < a + b :
    print('As retas formam um triangulo')
else :
    print('As retas não formam um triangulo')