# Problema 3047 - Beecrowd - Iniciante - Nível 1

# Inicialmente, recebemos os valores da Dona Mônica e dois filhos
monica = int(input())
filhoA = int(input())
filhoB = int(input())

# Calculamos a idade do terceiro filho
filhoC = monica - (filhoA + filhoB)

# A função max() imprime o maior valor dos argumentos passados
print(max(filhoA, filhoB, filhoC))