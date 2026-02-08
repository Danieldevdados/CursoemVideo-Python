v = []
ult = ini = mei = 0
for c in range(0,5):
    n = (int(input('Digite um valor:')))
    if c == 0 or n > v[-1]:
        v.append(n)
        print('Valor adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(v):
            if n <= v[pos]:
                v.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(f'Valores digitados em ordem foram {v}')