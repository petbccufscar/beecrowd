# Problema 1865 - Beecrowd - Iniciante - Nível 1

# Leitura do número de casos
casos = int(input())
# Laço de repetição para cada caso
for i in range(casos):
    # Leitura do nome da personagem e da força empregada ao levantar o martelo
    nome, forca = input().split(' ')
    # Caso o nome digitado seja igual a "Thor", efetua-se um print do caractere 'Y'
    if nome == "Thor":
        print('Y')
    # Caso o nome seja qualquer outro, efetua-se um print do caractere N
    else:
        print('N')
