# Problema 1248 - Beecrowd - String - Nível 2

# Número de casos de teste
n = int(input())

# Para cada caso
for _ in range(n):
	# Criamos um conjunto a partir de cada entrada
	dieta  = set(input())
	café   = set(input())
	almoço = set(input())

	# Fazemos as operações que nos convém com os conjuntos
	comeu  = café | almoço
	extra  = comeu - dieta
	faltou = dieta - comeu

	# Verificamos se algo extra foi comido
	if extra != set():
		# Se sim, mostramos 'CHEATER'
		print('CHEATER')
	else:
		# Se não, mostramos o que faltou
		print(''.join(sorted(faltou)))
