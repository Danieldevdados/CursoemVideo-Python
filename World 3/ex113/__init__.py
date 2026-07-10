def leiaInt(msg):
    """

    :param msg:Numero que o usuario digitar
    :return: Valor inteiro
    """
    while True:
       try:
           v = int(input(msg))
       except Exception:
           print(f'\033[31mErro: por favor digite um numero inteiro valido!\033[m')
       except KeyboardInterrupt:
           print('\n\033[31mO usuario preferiu não digitar este numero!\033[m')
           return 0
       else:
           v = int(v)
           return v


def leiaFloat(msg):
    """

    :param msg:Numero que o usuario digitar
    :return: Valor inteiro
    """
    while True:
        try:
            v = float(input(msg))
        except Exception:
            print(f'\033[31mErro: por favor digite um numero Real valido!\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuario preferiu não digitar este numero!\033[m')
            return 0
        else:
            v = float(v)
            return v