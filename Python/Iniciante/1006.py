# Problema 1006 - Beecrowd - Iniciante - Nível 2


# Recebemos os 3 valores de entrada, já utilizando a função float para convertê-los, já que em python todo input retorna uma string
A = float(input())
B = float(input())
C = float(input())

# Em seguida, calculamos a média utilizando os pesos descritos no exercício e por fim a imprimimos com apenas uma casa decimal
media = (A*2 + B*3 + C*5)/10

print(f"MEDIA = {media:.1f}")