# Problema 1049 - Beecrowd - Iniciante - Nível 3

# Vamos receber primeiro as três strings, antes de classificar
filo = input()
classe = input()
alimentacao = input()

# Agora, vamos classificar utilizando IF's aninhados:
if filo == 'vertebrado':
    if classe == 'ave':
        if alimentacao == 'carnivoro':
            print('aguia')
        elif alimentacao == 'onivoro':
            print('pomba')
    elif classe == 'mamifero':
        if alimentacao == 'onivoro':
            print('homem')
        elif alimentacao == 'herbivoro':
            print('vaca')

elif filo == 'invertebrado':
    if classe == 'inseto':
        if alimentacao == 'hematofago':
            print('pulga')
        elif alimentacao == 'herbivoro':
            print('lagarta')
    elif classe == 'anelideo':
        if alimentacao == 'hematofago':
            print('sanguessuga')
        elif alimentacao == 'onivoro':
            print('minhoca')