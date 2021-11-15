# Problema 1099 - Beecrowd - Iniciante - Nível 1

# Leitura da variável 'n' (número de testes que serão feitos)
n = int(input())

# Declaração da variável soma
soma = 0

# Início do primeiro loop
for contador1 in range(n):
	
	# Leitura das variáveis 'x' e 'y'
	x,y = map(int, input().split(' '))
  
	# Condicional caso 'y' seja maior que 'x'
	if(y>x):

		# Calculando quantas vezes ocorrerá o próximo loop
		k = y-x

		# Início do segundo loop
		for contador2 in range(k-1):

			# Incrementando a variável 'x' em 1
			x=x+1

			# Testando para ver se é ímpar
			if (x%2 != 0):

				# Somando caso for ímpar
				soma = soma + x


		# Printando a soma dos ímpares entre 'x' e 'y'
		print(soma)

		# Zerando a soma para o próximo teste
		soma=0
  
	# Caso 'x' seja maior que 'y'
	else:

		# Calculando quantas vezes ocorrerá o próximo loop
		k = x-y

		# Início do terceiro loop
		for contador3 in range(k-1):
			# Incrementando a variável 'y' em 1
			y=y+1

			# Testando para ver se é ímpar
			if (y%2 != 0):

				# Somando caso for ímpar
				soma = soma + y

		# Printando a soma dos ímpares entre 'x' e 'y'		
		print(soma)

		# Zerando a soma para o próximo teste
		soma=0