# Problema 2950 - URI - Iniciante - Nível 1

# Inicializa as variáveis e atribui
# os valores da distância entre os Palantír's
# e os seus respectivos diâmetros
Distancia, Diametro1, Diametro2 = map(int, input().split(' '))

# Imprime a ICM
print("{:.2f}".format(Distancia/(Diametro1 + Diametro2)))
