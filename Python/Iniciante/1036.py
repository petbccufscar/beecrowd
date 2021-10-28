# Problema 1036 - URI - Iniciante - Nível 3

# Importa o módulo com funções matemáticas básicas
import math

# Leitura dos valores
A, B, C = [float(i) for i in input().split()]

# Verifica se existe raiz real para essa equação
if (pow(B, 2) - 4*A*C) > 0 and A != 0:
    # Cálculo das raízes
    R1 = (-B + math.sqrt(pow(B, 2) - 4*A*C))/(2*A)
    R2 = (-B - math.sqrt(pow(B, 2) - 4*A*C))/(2*A)

    # Imprime as raízes na saída padrão
    print("R1 = {:.5f}".format(R1))
    print("R2 = {:.5f}".format(R2))
else:
    # Caso não exista raíz real
    print("Impossivel calcular")
