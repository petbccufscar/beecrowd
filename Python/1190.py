# Problema 1190 - URI - Iniciante - Nível 1

# Leitura da operação
operacao = input()

# Criação da matriz e leitura dos números
matriz = []
for i in range(12):
  # Criando as demais dimensões
  matriz.append([])
  for j in range(12):
    matriz[-1].append(float(input()))

# Declarando a variável que armazenará o resultado
resultado = 0

# Realizando a soma dos elementos
for i in range(12):
  for j in range(12):
    if(i<j and i > 12 - j - 1):
      resultado += matriz[i][j]

# Conferindo qual operação a ser realizada
if operacao == 'M':
  resultado = resultado / 30.0

# Imprimindo resultado final
print(resultado)
