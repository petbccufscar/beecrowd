# Problema 1589 - URI - Iniciante - Nível 1

# Leitura do número de testes
T = int(input())

# Aqui usamos o _ pois o valor não tem importância
for _ in range(T):
	# Então lemos os raios
	R1, R2 = map(int, input().split(' '))
	
	# E printamos a soma
	print(R1 + R2)