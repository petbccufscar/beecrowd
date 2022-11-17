# Problema 2310 - Beecrowd - Iniciante - Nível 2

# Número de jogadores
n = input()

total_tentativas = [0, 0, 0]
total_sucessos = [0, 0, 0]

for i in range(n):
    # Vamos receber e ignorar o nome do jogador
    input()

    tentativas = map(int, input.split())
    total_tentativas = [x + y for x, y in zip(tentativas, total_tentativas)]

    sucessos = map(int, input().split())
    total_sucessos = [x + y for x, y in zip(sucessos, total_sucessos)]




