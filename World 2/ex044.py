preço = float(input('Digite o preço do produto : '))
print(''' Formas de pagamento : 
 1 - A vista = 10% 
  2 -  A vista no cartão = 5% 
   3 - Ate 2x no cartão 
   4- 3x ou mais no cartão = 20% juros ''')
pagamento = int(input('Digite a forma de pagamento : '))
if pagamento == 1 :
        desconto = preço * 0.10
        preçocomdesconto = preço - desconto
        print('O valor ficou {}'.format(preçocomdesconto))
elif pagamento == 2:
        desconto = preço * 0.05
        preçocomdesconto = preço - desconto
        print('O valor ficou {}'.format(preçocomdesconto))
elif pagamento == 3:
        print('O preço fica {} em ate 2x sem juros '.format(preço))
elif pagamento == 4:
        juros = preço * 0.20
        preçocomjuros = preço + juros
        print('O novo preço ficou {} '.format(preçocomjuros))
else:
        print('Opção invalida')
