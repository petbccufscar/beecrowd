# Problema 1044 - Beeccrowd - Iniciante - Nível 2

# Recebe os valores na entrada padrão
valorA, valorB = map(float, input().split())

# Verifica a divisibilidade para saber se são múltiplos ou não
if valorA%valorB == 0 or valorB%valorA == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
