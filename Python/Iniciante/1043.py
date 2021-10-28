# Problema 1043 - URI - Iniciante - Nível 2

# Recebe o módulo de cada lado
ladoA, ladoB, ladoC = [float(i) for i in input().split()]

# Verifica se é possível formar um triângulo com os valores informados
if not(ladoA + ladoB <= ladoC) and\
not(ladoA + ladoC <= ladoB) and\
not(ladoB + ladoC <= ladoA):
    print("Perimetro = {:.1f}".format(ladoA + ladoB + ladoC))

# Imprime a área do trapézio caso os lados não formem triângulo
else:
    print("Area = {:.1f}".format((ladoA + ladoB)*ladoC/2))
