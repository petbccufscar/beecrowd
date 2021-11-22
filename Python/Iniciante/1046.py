# Problema 1046 - Beecrowd - Iniciante - Nível 2

# Recebe a hora de inicio e a hora de finalização do jogo
inicio, fim = map(int, input().split())

# Se a hora de inicio for maior que a hora de finalização do jogo, então
# o jogo terminou no dia seguinte ao início, logo: horas úteis no dia do
# início é igual a (24 - inicio), considerando as horas jogadas no dia seguinte
# o tempo total é igual a (24 - inicio + fim).
if inicio >= fim:
    print("O JOGO DUROU {:d} HORA(S)".format(24 - inicio + fim))

# Se o jogo começou e terminou no mesmo dia, basta calcular a diferença
# entre a hora da finalização e a hora de inicio.
else:
    print("O JOGO DUROU {:d} HORA(S)".format(fim - inicio))
