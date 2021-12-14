# Problema 1049 - Beecrowd - Iniciante - Nível 3

# Vamos receber primeiro as três strings, antes de classificar
stringA = input()
stringB = input()
stringC = input()

# Agora, vamos classificar utilizando IF's aninhados:
if stringA == 'vertebrado':
    if stringB == 'ave':
        if stringC == 'carnivoro':
            print('aguia')
        elif stringC == 'onivoro':
            print('pomba')
    elif stringB == 'mamifero':
        if stringC == 'onivoro':
            print('homem')
        elif stringC == 'herbivoro':
            print('vaca')

elif stringA == 'invertebrado':
    if stringB == 'inseto':
        if stringC == 'hematofago':
            print('pulga')
        elif stringC == 'herbivoro':
            print('lagarta')
    elif stringB == 'anelideo':
        if stringC == 'hematofago':
            print('sanguessuga')
        elif stringC == 'onivoro':
            print('minhoca')