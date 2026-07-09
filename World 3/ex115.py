from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep
arq = 'Bancodepessoas.txt'

if not ArquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        Nome = str(input('Nome: '))
        Idade = leiaInt('Idade: ')
        cadastrar(arq, Nome, Idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema.....Ate logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção valida!\033[m')
        sleep(2)
