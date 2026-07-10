sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F] : ')).upper().strip()
    if sexo != 'M' and sexo != 'F':
        print('Dados invalidos, tente novamente!')
print('Sexo registrado {}'.format(sexo))