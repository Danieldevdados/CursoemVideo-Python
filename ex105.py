def notas(*n, sit=True):
    """

    :param n:Notas dentro da variavel resp
    :param sit: Situação opcional(False = Não mostra situação, True=  mostra situação)
    :return:Dicionario com as notas e situacao do aluno
    """
    geral = dict()
    geral['total'] = len(n)
    geral['maior'] = max(n)
    geral['menor'] = min(n)
    geral['media'] = sum(n) / len(n)
    if sit == True:
        if geral['media'] >= 7:
            geral['situacao'] = 'BOA'
        elif geral['media'] >= 5:
            geral['situacao'] = 'RAZOAVEL'
        else:
            geral['situacao'] = 'RUIM'
    print('-='*20)
    return geral



#Programa principal
resp = notas(10, 8, 10, 6.5,sit = True)
print(resp)
help(notas)