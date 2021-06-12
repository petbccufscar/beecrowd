# Problema 1015 - URI - Iniciante - Nível 1

# Adicionando "math" para usar "sqrt"
from math import sqrt

# Lendo x1 e y1
x1, y1 = map(float, input().split(" "))

# Lendo x2 e y2
x2, y2 = map(float, input().split(" "))

# Imprimindo a distância
print(f'{(sqrt((x2 - x1)**2 + (y2 - y1)**2)):.4f}')
