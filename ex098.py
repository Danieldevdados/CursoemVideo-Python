from time import sleep
def contador(i, f, p):
    c = 0
    print('-=' * 20)
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    print('-=' * 20)
    if i < f:
        while c <= f:
            print(f'{c}',end=' ')
            c += p
            sleep(0.5)

    else:
        while i >= f:
            print(f'{i}',end=' ')
            i -= p
            sleep(0.5)
    print('PRONTO!')

contador(1,10,1)
contador(10,0,2)
print('-=' * 20)
print('CONTAGEM PERSONALIZADA')
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)