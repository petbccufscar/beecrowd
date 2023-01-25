#Recebe os valores de entrada
entrada = input().split()

#Separa os valores entre linha e colunas
linhas, colunas = int(entrada[0]), int(entrada[1])

#Inicializa a matriz como uma lista vazia
matriz = list()

#Preenche a matriz
for i in range(linhas):
    matriz.append(list(map(int, input().split())))

x = 0
y = 0

#Percorre a matriz até achar o 42 e verifica todos os termos ao redor dele, e caso seja tudo 7,
#anota as coordenadas do matriz em x e y
for i in range(1, linhas-1):
    for j in range(1, colunas-1):
        if matriz[i][j] == 42:
             if matriz[i-1][j-1] == 7 and matriz[i-1][j] == 7 and matriz[i-1][j+1] == 7:
                if matriz[i][j-1] == 7 and matriz[i][j + 1] == 7:
                    if matriz[i+1][j-1] == 7 and matriz[i+1][j] == 7 and matriz[i+1][j+1] == 7:
                        x = i+1
                        y = j+1
                        break

#Imprime as coordenadas
print(f"{x} {y}")
