listagem = ('Lapis', 1.50 , 'Borracha', 2.0, 'Caderno', 20,
            'Mouse', 50, 'Teclado' , 55, 'Monitor', 800, 'PC gamer' , 1870)
print('-=' * 20)
print('LISTAGEM DE PREÇOS')
print('-='* 20)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]}..........', end='')
    else:
        print(f'R$ {listagem[item]}')