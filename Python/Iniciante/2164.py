# Problema 2164 - Beecrowd - Iniciante - Nível 2

# Vamos precisar da função de raiz quadrada do pacote de matemática
import math

# Definindo uma função fibonacci usando a fórmula
def fibonacci(n):
    r5 = math.sqrt(5) # Apenas para facilitar a leitura da fórmula abaixo
    return (((1+r5)/(2))**n - ((1-r5)/(2))**n)/(r5)

# Input do usuário
n = float(input())

# Retornando fibonacci com a precisão requerida
print(f"{fibonacci(n):.1f}")