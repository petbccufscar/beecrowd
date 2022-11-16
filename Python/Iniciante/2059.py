# Problema 2059 - Beecrowd - Iniciante - Nível 2

#Recebe a entrada e a divide em 5 partes diferentes, já que cada uma representa uma coisa diferente
par, num1, num2, roubo1, roubo2 = map(int, input('').split())

#Verifica se o jogador 2 acusou falsamente o jogador 1 e imprime o resultado
if roubo1 == 0 and roubo2 == 1:
    print ('Jogador 1 ganha!')
    exit()

#Verifica se ele roubou e foi descoberto e imprime o resultado
if roubo1 == 1 and roubo2 == 1:
    print ('Jogador 2 ganha!')
    exit()

#Verifica se o jogador 1 roubou e o 2 não o acusou
if roubo1 == 1 and roubo2 == 0:
    print ('Jogador 1 ganha!')
    exit()


#Faz a soma dos números colocados pelos jogadores
soma = (num1+num2)

#Verifica se o número é par e se for entra no loop
if (soma % 2) == 0:

    #Verifica se o jogador 1 escolheu par
    if par == 1:
        print ('Jogador 1 ganha!')
        
    #Verifica o jogador tenha escolhido ímpar e imprime o resultado
    elif par == 0:
        print ('Jogador 2 ganha!')

#Verifica se o número é ímpar
if (soma % 2) == 1:

    #Verifica se o jogador 1 escolheu ímpar
    if par == 0:
        print ('Jogador 1 ganha!')

    #Verifica o jogador tenha escolhido par e imprime o resultado
    elif par == 1:
        print ('Jogador 2 ganha!')