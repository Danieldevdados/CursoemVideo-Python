def area(l, c):
    area = l * c
    print(f'A area é {area}m²')


print('-='* 20)
print('CONTROLE DE TERRENOS')
print('-='*20)
largura = float(input('LARGURA (m) : '))
comprimento = float(input('COMPRIMENTO (m) : '))
area(largura, comprimento)