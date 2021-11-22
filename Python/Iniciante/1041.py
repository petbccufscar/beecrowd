# Problema 1041 - Beecrowd - Iniciante - Nível 3

# Recebe as coordenadas do ponto
x, y = map(float, input().split())

# Verifica em qual quadrante, ou eixo, o ponto está
# e imprime o resultado na saída padrão
if x == 0 and y == 0:
    print("Origem")
elif x == 0:
    print("Eixo Y")
elif y == 0:
    print("Eixo X")
elif x > 0 and y > 0:
    print("Q1")
elif x > 0 and y < 0:
    print("Q4")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
