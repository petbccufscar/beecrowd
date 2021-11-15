# Problema 2006 - Beecrowd - Iniciante - Nível 1

# Entrada da numeração do chá correto
n = int(input())

# Recebemos todos os palpites em uma única linha e o dividimos com split(), com o map convertemos todos para int e
# transformamos em uma lista de palpites.
respostas = list(map(int, input().split(' ')))

# Quantidade de acertos iniciada em 0
acertos = 0

# Para cada resposta dada, verificamos se é a resposta correta e incrementamos o contador de acertos
for resposta in respostas:
    if(int(resposta) == n):
        acertos += 1

# Por fim, exibe-se a quantidade de acertos
print(acertos)