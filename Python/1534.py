# Problema 1534 - URI - Iniciante - Nível 1

# Loop responsável pelos casos de testes
while True:
  try:
    # Orde da matrizes
    ordem = int(input())
    # Criação da matriz e leitura dos números
    matriz = []
    for i in range(ordem):
      # Criando as demais dimensões
      auxiliar = []
      for j in range(ordem):
        if(i + j == ordem - 1):
          auxiliar.append(2)
        elif(i == j):
          auxiliar.append(1)
        else:
          auxiliar.append(3)
      matriz.append(auxiliar)
    # Imprimindo a matriz
    for i in range(ordem): 
      for j in range(ordem):
        print(matriz[i][j], end = '')
      print() 
  # Caso de exceção chegar ao EOF
  except:
    break