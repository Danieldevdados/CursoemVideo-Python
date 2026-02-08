palavra = str(input('Digite uma palavra : ')).strip().lower()
palavras = palavra.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Ele é um palindromo')
else:
    print('Ele não é um palindromo')