from uteis import moeda

p = float(input('Digite o preço :  R$'))
print(f'A metade de {moeda.moeda2(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda2(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando em 10% fica {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 13% fica {moeda.diminuir(p, 13, False)}')