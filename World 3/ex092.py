from datetime import date
geral = dict()
geral['nome'] = str(input('Nome: '))
anodenascimento = int(input('Ano de nascimento : '))
geral['idade'] = date.today().year - anodenascimento
geral['ctps'] =int(input('Carteira de Trabalho : [0 não tem] '))
if geral['ctps'] != 0:
    geral['contracacao'] =  int(input('Ano de contratação : '))
    geral['salario'] = float(input('Salario : '))
    geral['aposentadoria'] = geral['idade'] + ((geral['contracacao'] + 35) - date.today().year)
    print('-='* 20)
for k,v in geral.items():
    print(f'{k} tem o valor de {v}')