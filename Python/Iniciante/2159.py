# Problema 2159 - Beecrowd - Iniciante - Nível 1

# Importando o pacote math para utilizar a função log(elemento, base)
import math

# Leitura da variável de entrada
n = float(input())

# Cálculo do valor máximo
minimo=n/math.log(n,2.718281828459045235360287)

# Cálculo do valor mínimo
maximo=1.25506*(n/math.log(n,2.718281828459045235360287))

# Printando o resultado
print(f'{minimo:.1f} {maximo:.1f}')

