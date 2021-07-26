# Problema 3209 - URI - Iniciante - Nível 1

# Leitura do número de testes
n = int(input())

# Leitura dos testes
for i in range(n):
	k, *filtros = map(int, input().split())

	# O número total de tomadas disponível é:
	#   Soma das tomadas de todos os filtros
	#   Menos as tomadas em que serão ligados os filtros
	#   Mais a tomada da parede
	print(sum(filtros) - k + 1)