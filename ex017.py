from math import hypot
cop = float(input('Digite o comprimento do cateto oposto : '))
cad = float(input('Digite o comprimento do cateto adjacente : '))
hipotenusa = hypot(cop,cad)
print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))

