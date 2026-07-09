n1 = int(input('Digite um numero : '))
print('''Qual sera a base de conversão ? 
1 - BINARIO
2 - OCTAL
3 - HEXADECIMAL''')
opcao = int(input('Sua opção : '))
if opcao == 1:
    binario = bin(n1)[2:]
    print(binario)
elif opcao == 2:
    octal = oct(n1)[2:]
    print(octal)
elif opcao == 3:
    hexadecimal = hex(n1)[2:]
    print(hexadecimal)
else:
    print('Opção invalida')
