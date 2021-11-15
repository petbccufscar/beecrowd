# Problema 1013 - Beecrowd - Iniciante - Nível 3

# Vamos definir a função que retorna o maior valor
def maior(a, b):
	return int((a + b + abs(a - b)) / 2)

# Então lemos os três valores
a, b, c = map(int, input().split())

# E printamos o maior
print(f'{maior(maior(a, b), c)} eh o maior')