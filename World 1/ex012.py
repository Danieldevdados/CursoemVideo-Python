pr = float(input('Digite o valor do produto: '))
ds = float(input('Digite o valor do desconto: '))
nv = pr * ds / 100
print('O novo valor sera {} $'.format(pr - nv))