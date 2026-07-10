def leiaInt(msg):
    """

    :param msg:Numero que o usuario digitar
    :return: Valor inteiro
    """
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro ! Digite um numero inteiro valido.\033[m')
        if ok == True:
            break
    return valor




#Programa principal
n = leiaInt('Digite um numero inteiro : ')
print(f'Você acabou de digitar o numero {n}')