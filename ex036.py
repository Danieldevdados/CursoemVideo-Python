from time import sleep

print('-=-=-=-=-=-=-=-=-=-=-=-=-CORRETORA-=-=-=-=-=-=-=-=-=-=-=-=-')

valor = int(input('Digite o valor da casa: '))
sleep(0.20)
salario = float(input('Digite o seu salário: '))
sleep(0.20)
anos = int(input('Em quantos anos você vai pagar? '))
sleep(0.20)

meses = anos * 12
vlc = valor / meses
juros = salario * 0.3
sleep(0.50)

# Cores: \033[0;32m (verde)  \033[0;31m (vermelho)  \033[m (reset)
print(f'\nPrestação mensal: \033[0;32mR$ {vlc:.2f}\033[m')
print(f'30% do salário: R$ {juros:.2f}')

if vlc <= juros:
    print('\033[0;32m✅ EMPRESTIMO CONCEDIDO\033[m')
else:
    print('\033[0;31m❌ EMPRESTIMO NEGADO \033[m')
