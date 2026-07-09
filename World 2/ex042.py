print('-=' * 20)
print('ANALISADOR DE TRIANGULOS')
print('-=' * 20)
a = int(input('Digite a primeiro segmento : '))
b = int(input('Digite a segundo segmento : '))
c = int(input('Digite a terceiro segmento : '))
if a < b + c and b < a + c and c < a + b :
    print('As retas formam um triangulo')
    if a == b and b == c:
        print('Equilátero')
    elif a == b or a == c or b == c:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('As retas não formam um triângulo')