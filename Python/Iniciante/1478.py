# Problema 1478 - Beecrowd - Iniciante - Nível 1

# Lendo as ordens das matrizes
ordens = []

# Variável auxiliar para controle das leitura das ordens
aux = 1
while(aux != 0):
  aux = int(input())
  if aux != 0:
    ordens.append(aux)

# Procedendo o programa para cada ordem
for ordem in ordens:
  # Criação da matriz e leitura dos números
  matriz = []
  for i in range(ordem):
    # Criando as demais dimensões
    auxiliar = []
    for j in range(ordem):
      if(i == j):
        auxiliar.append(1)
      if(i > j):
        auxiliar.append(i - j + 1)
      if(i < j):
        auxiliar.append(j - i + 1)
    matriz.append(auxiliar)

  # Imprimindo a matriz
  for i in range(ordem): 
    for j in range(ordem):
      if j == 0:
        print(f"{matriz[i][j]:3d}", end = "") 
      else:
        print(f" {matriz[i][j]:3d}", end = "") 
    print() 
  print()
