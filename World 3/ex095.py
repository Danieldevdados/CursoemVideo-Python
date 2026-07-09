informacoes = dict()
while True:
    informacoes['nome'] = str(input('Nome do jogador : '))
    partidas = int(input(f'Quantas partidas {informacoes["nome"]} jogou ? '))
    informacoes['gols'] = list()
    informacoes['total'] = 0
    for c in range(partidas):
        gols = int(input(f'Quantos gols na partida {c} ? '))
        informacoes['gols'].append(gols)
        informacoes['total'] += gols
    resp = str(input('Quer continuar ? [S / N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S / N] ')).strip().upper()[0]
    if resp =='N':
        break
    print(informacoes)
    print('-=' * 20)
    print(f'O campo nome tem o valor de {informacoes["nome"]}')
    print(f'O campo gols tem o valor de {informacoes["gols"]}')
    print(f'O campo total tem o valor de {informacoes["total"]}')
print('-=' * 20)
print(f'O jogador {informacoes["nome"]} jogou {partidas} partidas')
for p, g in enumerate(informacoes['gols']):
    print(f'=> Na partida {p}, fez {informacoes["gols"][p]} gols.')
print(f'foi um total de {informacoes["total"]} gols')