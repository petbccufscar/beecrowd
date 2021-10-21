# Problema 1253 - URI - String - Nível 3

# Número de casos de teste
n = int(input())

# Para cada caso de teste
for _ in range(n):
	# Lemos a sentença e a posição
	sentença = input()
	posição  = int(input())

	# Para cada caractere na sentença
	for c in sentença:
		# Transformamos o caractere em número (ASCII)
		c = ord(c)
		# Subtraímos o número base (A vale 65 em ASCII, assim A passa a valer 0, B vale 1, etc)
		c = c - 65
		# Subtraímos a posição
		c = c - posição
		# Aplicamos módulo para não sair dos números do alfabeto
		c = c % 26
		# Somamos 65 (A passa a valer 65, B vale 66, etc)
		c = c + 65
		# Transformamos o número em caractere novamente
		c = chr(c)
		# Printamos
		print(c, end='')

	print()