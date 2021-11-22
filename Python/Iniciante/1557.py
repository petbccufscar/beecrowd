# Problema 1557 - Beecrowd - Iniciante - Nível 1

# Usaremos as funções log e ceil
from math import log, ceil

while True:
	# Leitura do tamanho da matriz
	T = int(input())

	# Sairemos do loop quando o tamanho for 0
	if T == 0:
		break

	# Usaremos o maior valor para calcular o tamanho do alinhamento
	# Os números são potências de 2, especificamente a soma de suas coordenadas
	# A coordenada do último número é T - 1 em ambos os eixos
	maior = 2**(2*(T - 1))
	
	# Usamos log com base 10 para calcular o número de casas do maior número
	# ceil arredonda para cima, como o retorno de ceil é float, convertemos com int
	casas = int(ceil(log(maior, 10)))

	# Para cada linha
	for i in range(T):
		# Auxiliar para a margem
		# Os números são separados com espaço
		# Não há espaço após o último número
		margem = ''
		
		# Para cada coluna
		for j in range(T):
			# Calculamos o valor
			valor = 2**(i+j)
			
			# Printamos o valor, usando o número de casas previamente calculado
			# O valor padrão de 'end' é '\n', por conta do alinhamento, vamos omiti-lo
			print(f'{margem}{valor:{casas}}', end='')
			
			# Como estamos printando a margem antes do número, apenas o primeiro não a possui
			margem = ' '
		
		print()
	
	print()
