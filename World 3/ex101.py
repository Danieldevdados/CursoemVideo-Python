def voto():
    from datetime import date
    print('-'*40)
    anodenasc = int(input('Digite o ano de seu nascimento: '))
    idade = date.today().year - anodenasc
    if idade >= 18:
        return 'VOTO OBRIGATORIO'
    elif idade == 16 or idade == 17 or idade >= 70:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO NEGADO'




v = voto()
print(f'{v}')