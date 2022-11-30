#Problema 1178 - Beecrowd - Iniciante - Nível 2

# Leitura do valor de x
x = float(input())

#Colocando o primeiro valor no vetor
N = [x]

#Mostrando o primeiro valor do vetor
print(f"N[0] = {N[0]:.4f}") 

#Criação de um loop que preencherá o vetor com os 99 elementos restantes
for i in range(1,100):

    #Divisão do valor de x por dois para que o próximo elementa de N receba metade do valor atual de x
    x = x/2
    #Acréscimo do valor de x no final o vetor N
    N.append(x)
    #Printando os valores do vetor.
    print(f"N[{i}] = {N[i]:.4f}") 