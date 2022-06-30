# Problema 2059 - Beecrowd - Iniciante - Nível 2

#A resposta 18 do beecrowd está incorreta, testei tanto pelo código quanto vendo pela lógica

#Recebe a entrada e a divide em 5 partes diferentes, já que cada uma representa uma coisa diferente
par, num1, num2, roubo1, roubo2 = map(int, input('').split())

#Faz a soma dos números colocados pelos jogadores
soma = (num1+num2)

#Verifica se o número é par e se for entra no loop
if (soma % 2) == 0:

    #Verifica se o jogador 1 escolheu par
    if par == 1:
        
        #Verifica se ele não roubou e imprime o resultado
        if roubo1 == 0:
            print ('Jogador 1 ganha!')

        #Verifica se ele roubou e foi descoberto e imprime o resultado
        elif roubo1 == 1 & roubo2 == 1:
            print ('Jogador 2 ganha!')

        #Verifica o jogador 2 não ache que o 1 roubou e imprime o resultado
        elif roubo2 == 0:
            print ('Jogador 1 ganha!')
    
    #Verifica o jogador tenha escolhido ímpar e imprime o resultado
    elif par == 0:
        print ('Jogador 2 ganha!')

#Verifica se o número é ímpar
if (soma % 2) == 1:

    #Verifica se o jogador 1 escolheu ímpar
    if par == 0:

#Os passos abaixo fazem as mesmas verificações que o if de cima        
        if roubo1 == 0:
            print ('Jogador 1 ganha!')
        elif roubo1 == 1 & roubo2 == 1:
            print ('Jogador 2 ganha!')
        elif roubo2 == 0:
            print ('Jogador 1 ganha!')

    #Verifica o jogador tenha escolhido par e imprime o resultado
    elif par == 1:
        print ('Jogador 2 ganha!')