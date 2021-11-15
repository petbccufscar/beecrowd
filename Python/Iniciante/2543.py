# Problema 2543 - Beecrowd - Iniciante - Nível 1

# Usaremos a entrada padrão diretamente
from sys import stdin

# Como o arquivo de entrada termina com EOF, definimos esse auxiliar para abstrair a leitura dos casos
def casos():
	# N indica o número de linhas restantes de um caso
	N = 0
	# Identificador do autor em questão
	identificador = 0
	# Lista com as informações dos gameplays
	gameplays = []

	# Para cada linha na entrada padrão
	for linha in stdin:
		# Removemos o \n no final da linha
		linha = linha.strip()

		# Se todas as linhas de um caso foram lidas
		if N == 0:
			# Essa linha é referente a um novo caso
			# O que significa que o anterior terminou
			# Se o identificador é válido, emitimos os valores do último caso
			if identificador != 0:
				yield identificador, gameplays

			# Continuamos processando os dados desse caso
			# Lemos o número de gameplays e o identificados do autor
			N, identificador = map(int, linha.split(' '))
			# Resetamos a lista de gameplays
			gameplays = []

		# Se ainda precisamos ler as linhas de um caso
		else:
			autor, jogo = map(int, linha.split(' '))
			gameplays.append((autor, jogo))
			N -= 1

	# Quando as linhas acabarem, significa que o último caso terminou
	# Emitimos os dados referentes à ele
	yield identificador, gameplays

# Para cada caso de teste
for identificador, gameplays in casos():
	# Definimos o contador para 0
	contador = 0
	
	# Verificamos os dados pré-processados
	for autor, jogo in gameplays:
		# Se o gameplay é do autor em questão e o jogo é CSGO
		if identificador == autor and jogo == 0:
			# Incrementamos
			contador += 1

	# No fim de cada caso printamos o contador de gameplays
	print(contador)