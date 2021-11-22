# Problema 1257 - Beecrowd - String - Nível 3

# Número de casos de teste
n = int(input())

# Para cada caso de teste
for _ in range(n):
	# Lemos o número de linhas
	l = int(input())

	# Valor da hash
	h = 0

	# Para cada linha
	for elemento in range(l):
		# Lemos a linha
		linha = input()

		# Para cada caractere da linha
		for posição, c in enumerate(linha):
			# Somamos à hash
			#	O valor do caractere
			#	O índice do elemento
			#	A posição
			h += (ord(c) - 65) + elemento + posição

	# Printamos o valor da hash
	print(h)
