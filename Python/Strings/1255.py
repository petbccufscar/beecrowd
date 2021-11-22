# Problema 1255 - Beecrowd - String - Nível 3
from collections import defaultdict

# Número de casos de teste
n = int(input())

# Para cada caso de teste
for _ in range(n):
	# Lemos a linha
	linha = input()
	# Convertemos todos os caracteres para minúsculas
	linha = linha.lower()
	# Filtramos só as letras
	linha = filter(lambda c : c.isalpha(), linha)

	# Flag para letra mais recorente	
	maior = 0

	# Contamos as letras
	contador = defaultdict(int)
	for c in linha:
		# Incrementamos o valor atual
		atual = contador[c] + 1
		# Verificamos se ele é o novo maior
		maior = max(maior, atual)
		# Atribuímos o novo valor atual ao contador
		contador[c] = atual

	# Filtramos só as letras mais recorentes
	maiores = filter(lambda c : contador[c] == maior, contador)

	# Printamos em ordem alfabética
	print(''.join(sorted(maiores)))