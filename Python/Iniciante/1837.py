# Problema 1837 - Beecrowd - Iniciante - Nível 7

# Aqui, teremos que implementar o Algorítmo da Divisão,
# ou 'Teorema da Divisão Euclidiana'

# Inicialmente, vamos receber os valores de 'a' e 'b'
a, b = map(int, input().split(' '))

# Como método de resolução, iremos encontrar um resto 'r'
# inteiro, tal qual, o quociente 'q' seja inteiro.
# Pois pelo teorema, eles são únicos.
for r in range(abs(b)):
    q = (a - r)/b

    # Se o quociente 'q' for 0, já temos os dois valores únicos
    # e para evitar uma tentativa de divisão por 0, separamos
    # como um caso a parte.
    if q == 0:
        break

    # De resto, só verificamos se o quociente 'q' é um inteiro e 
    # divisivel pela soma do valor de 'a' mais o resto 'r'.
    elif a > 0:
        if (a + r) % q == 0:
            break
    elif a < 0:
        if (a - r) % q == 0:
            break

# É impresso o quociente 'q' como um inteiro, pois durante
# a divisão, ele assume o tipo 'float' e o resto 'r'.
print(int(q), r)