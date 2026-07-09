from uteis import moeda
p = float(input('Digite o preço :  R$'))
print(f'A metade de {moeda.moeda2(p)} é {moeda.moeda2(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda2(p)} é {moeda.moeda2(moeda.dobro(p))}')
print(f'Aumentado 10% de {moeda.moeda2(p)} fica {moeda.moeda2(moeda.aumentar(p, 10))}')
print(f'Diminuindo 13% de {moeda.moeda2(p)} fica {moeda.moeda2(moeda.diminuir(p, 13))}')