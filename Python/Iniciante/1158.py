# Problema 1158 - Beecrowd - Iniciante - Nível 1

# Lendo o valor de entrada inteiro
entrada = int(input())
# Loop dos testes
for i in range(entrada):
  # Lendo X e Y
  X, Y = map(int, input().split(" "))
  # Variável auxiliar e soma
  j = 0
  soma = 0
  # Loop para checagem de ímpares
  while j < Y:
    # Conferindo de o valor em X é ímpar
    if(X % 2 == 1):
      # Somando o valor de X a soma e incrementando o contador 
      soma += X
      j += 1
    # Incremetando o valor de X para prosseguir para o próximo valor ímpar
    X += 1
  # Imprimindo a soma final
  print(soma)
    
