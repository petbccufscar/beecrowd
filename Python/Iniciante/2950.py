# Inicializa as variáveis e atribui
# os valores da distancia entre os Palantír's
# e os seus respectivos diâmetros
Distancia, Diametro1, Diametro2 = [int(i) for i in input().split()]

# Imprime a ICM
print("{:.2f}".format(Distancia/(Diametro1 + Diametro2)))
