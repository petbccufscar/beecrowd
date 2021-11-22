# Problema 2879 - Beecrowd - Iniciante - Nível 1

# Lê a quantidade de valores
n = int(input())
partidas_perdidas = 0

for i in range(n):
    # Lê o número e verifica se é 1
    # Caso for, essa partida não será ganha
    if int(input()) == 1:
        partidas_perdidas += 1

# Imprime a quantidade de jogos ganhos
print(n - partidas_perdidas)