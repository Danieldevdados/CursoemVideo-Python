n = []
mai = 0
men = 0
for c in range(0, 5):
    n.append(int(input(f'Digite um valor para a posição {c} : ')))
    if c == 0:
        mai = men = n[c]
    else:
        if n[c] > mai:
            mai = n[c]
        if n[c] < men:
            men = n[c]

print('-=' * 20)
print(f'Você digitou os valores {n}')
print(f'O maior valor digitado foi {mai} na posição ', end='')
for i, v in enumerate(n):
    if v == mai:
        print(f'{i}')
print(f'O menor valor digitado  {men} foi na posição ', end='')
for i, v in enumerate(n):
    if v == men:
        print(f'{i}', end='')
