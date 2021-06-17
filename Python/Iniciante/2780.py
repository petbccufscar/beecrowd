# Problema 2780 - URI - Iniciante - Nível 1

# Entrada de dados, sendo o valor da distância do robô para a cesta
distancia = int(input())

# Testando se a distância é válida e apresentando a saída
if(distancia<0 or distancia>2000):
    print("Distância inválida")
else:
    if(distancia<=800):
        print("1")
    elif(distancia<=1400):
        print("2")
    else:
        print("3")