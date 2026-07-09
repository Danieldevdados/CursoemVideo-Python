dia = int(input('Quantos dias você usou o carro ? '))
km = float (input('Quantos km você rodou com ele ? '))
ttl = (dia * 60) + (km * 0.15)
print('O valor para pagar é R${:.2f}'.format(ttl))