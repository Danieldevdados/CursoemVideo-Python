while True:
    n = int(input('Quer ver a tabuada de qual valor ? '))
    if n >= 0:
        print('-' * 12)
        for t in range(1,11):
            print(f'{n} x {t} = {n * t}')
        print('-' * 12 )
    if n < 0:
        break
print('-' * 12)
print('PROGAMA TABUADA ENCERRADO...')