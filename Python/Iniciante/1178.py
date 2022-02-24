#Problema 1178 - Beecrowd - Iniciante - Nível 2

#Leitura do valor de x
x = float(input())

#Declaraçao do vetor N
N = []

#Criação de um loop que preencherá a matriz com os 100 elementos
for i in range(100):

    #Acréscimo do valor de x no final o vetor N
    N.append(x)
    #Divisão do valor de x por dois para que o próximo elementa de N receba metade do valor atual de x
    x = x/2

#Criação de um loop para printar os elementos de N
for i in range(100):
    #uso do truncamento da quarta casa decimal 
    print(f"N[{i}] = {N[i]:.4f}")