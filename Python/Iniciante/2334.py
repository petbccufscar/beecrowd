# Problema 2334 - Beecrowd - Iniciante - Nível 3

#Enquanto o -1 não for digitado, o programa contínua no loop
while True:

    #Recebe a entrada
    entrada = int(input())

    #Verifica se ela é -1 e se for, o programa encerra
    if(entrada == -1):
        exit()

    #Imprime o número da entrada - 1
    if(entrada != 0):
        print(entrada-1)
    else:  
        print(entrada)

    