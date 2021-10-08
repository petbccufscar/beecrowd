entrada = input().split()
inicio,final = [int(x) for x in entrada]

duracao = final - inicio

if (duracao < 0):
    duracao = 24 + (final - inicio)

if (inicio == final):
    print('O JOGO DUROU 24 HORA(S)')
else:
    print('O JOGO DUROU %d HORA(S)'%(duracao))
