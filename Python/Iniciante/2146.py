# Problema 2146 - Beecrowd - Iniciante - Nível 1

# Criando o loop para ler as variáveis até finalizar o arquivo(EOF)

while True:
	try:
		# Leitura da variável 'n'
		n=int(input())

		# Printando 'n-1'
		print(n-1)

	except EOFError:
		break