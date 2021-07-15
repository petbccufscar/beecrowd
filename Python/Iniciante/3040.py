# Problema 3040 - URI - Iniciante - Nível 1

# Recebendo o número de casos de testes do problema.
numTestes = int(input())

# Iniciando um vetor, que armazenará as respostas para os testes
respostas = []
for i in range(numTestes):
# Para cada teste, recebendo o valor da altura da árvore, o diámetro e a quantidade de galhos.
  alt, dmt, qtdGalhos = map(int, input().split(" "))

# Decidindo se os parámetros da árvore são adequados de acordo com o problema, e guardando a resposta em um vetor de respostas.
  if(alt>=200 and alt<=300 and dmt>=50 and qtdGalhos>=150):
    respostas.append("Sim")
  else:
    respostas.append("Nao")

# Apresentando as respostas
for i in range(numTestes):
  print(respostas[i])