cidade = str(input('Digite o nome de sua cidade : ')).strip()
print('A sua cidade começa com SANTO ? \n {}'.format(cidade[:5].upper() == 'SANTO'))