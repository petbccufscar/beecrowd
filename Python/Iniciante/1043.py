# Problema 1043 - Beecrowd - Iniciante - Nível 2

# Recebe o módulo de cada lado
ladoA, ladoB, ladoC = map(float, input().split())

# Verifica se é possível formar um triângulo com os valores informados
if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
    print(f"Perimetro = {(ladoA + ladoB + ladoC):.1f}")

# Imprime a área do trapézio caso os lados não formem triângulo
else:
    print(f"Area = {((ladoA + ladoB)*ladoC/2):.1f}")
