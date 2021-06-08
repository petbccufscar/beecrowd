# Problema 1172 - URI - Iniciante - Nível 1

# Definindo o vetor
X = []
# Lendo os valores do vetor
for i in range(0, 10):
  X.append(int(input()))
  # Conferindo os valores e substituindo nulos e negativos
  if(X[i] <= 0):
    X[i] = 1
# Imprimindo valores atualizados
for i in range(0, 10):
  print(f'X[{i}] = {X[i]}')
    