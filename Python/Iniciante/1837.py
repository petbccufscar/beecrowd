# Problema 1837 - Beecrowd - Iniciante - Nível 7

# Aqui, teremos que implementar o Algorítmo da Divisão,
# ou 'Teorema da Divisão Euclidiana'

# Inicialmente, vamos receber os valores de 'a' e 'b'
a, b = map(int, input().split(' '))

# Como método de resolução, iremos encontrar um resto 'r'
# da divisão de 'a' pelo valor absoluto de 'b'.
r = a % abs(b)

# Tendo o resto em mãos, é possível achar o quociente pela
# Teorema da Divisão Euclidiana dado por: a = b * q + r,
# isolando o 'q', temos que:
q = (a - r) / b

# É impresso o quociente 'q' como um inteiro, pois durante
# a divisão, ele assume o tipo 'float' e o resto 'r'.
print(int(q), r)