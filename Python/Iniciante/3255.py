# Problema 3255 - URI - Iniciante - Nível 1
# Adaptado da solução original, disponível em https://nordic.icpc.io/ncpc2011/

# Vamos achar todos os primos até 10008
N = 10008

# Vetor que marca quais valores são primos
p = [True] * N

# 0 e 1 não são primos
p[0] = False
p[1] = False

# Desmarca múltiplos de valores primos do vetor
for n in range(2, N):
	if (n * n) >= N:
		break

	if p[n]:
		for k in range(2*n, N, n):
			p[k] = False

# Lista com os números primos efetivamente
# Enumerate transformará os True e Falses em tuplas com seu respectivo número
# Ficando (0, False), (1, False), (2, True) ...
# A função lambda pegará o segundo valor de cada tupla, ou seja, o booleano
# Filter usará essa função e pegará apenas as tuplas que retornarem True, ou seja, os primos
# Zip fará uma tupla com os resultados obtidos do filter
# List retornará uma lista com uma tupla com todos os primos e outra com apenas valores True 
# [0] pegará a primeira parte da lista, os números primos
q = list(zip(*filter(lambda e : e[1], enumerate(p))))[0]

# Vetor solução para PD (programação Dinâmica)
# Inicializado com N
# O vetor tem tamanho '3*N'
# Pois tem a solução para cada número para cada jogador
D = [N] * (3*N)

# Construção do vetor solução

# Para cada número primo
for n in q:
	# O jogador da vez pode apenas dividir pelo número primo
	D[3*n] = 1

	# Para todos os números menores que esse, até o próximo primo
	for l in range(n - 1, 1, -1):
		# Encontramos o próximo primo
		if p[l]:
			break

		# O número 'l' não é primo, inicialmente a melhor jogada é somar 1
		# Então inicialmente a solução é igual a do número seguinte
		# Apenas rotacionada por conta da ordem dos jogadores (um turno foi gasto)
		D[3 * l + 0] = D[3 * (l + 1) + 2]
		D[3 * l + 1] = D[3 * (l + 1) + 0]
		D[3 * l + 2] = D[3 * (l + 1) + 1]

		# Mas pode ser que 'l' seja múltiplo de um primo
		# Para cada primo
		for k in q:
			# Se 'l' é múltiplo de 'k'
			if not l%k: # l%k == 0
				# Então podemos dividir por um primo 'k'
				# Mas precisamos verificar se esse caminho é melhor que o atual (somar 1)
				#
				# min(l // k, D[3 * (l // k) + 2])
				# Essa expressão basicamente leva em conta se esse é o último fator primo do número (primeiro termo)
				# Se não for (segundo termo), pega a melhor solução para o resultado, levando em conta a ordem de jogada (+2)
				if (min(l // k, D[3 * (l // k) + 2]) <= D[3 * l]):
					# Apenas atribuímos as respostas para cada jogador
					D[3 * l + 0] = min(l // k, D[3 * (l // k) + 2])
					D[3 * l + 1] =             D[3 * (l // k) + 0]
					D[3 * l + 2] =             D[3 * (l // k) + 1]

# Substituindo os números restante pelo número inicial (efetivamente o indíce)
# Que é a pontuação atribuída a quem não consegue jogar na rodada
for n in range(1, N):
	D[3 * n + 0] = min(n, D[3 * n + 0])
	D[3 * n + 1] = min(n, D[3 * n + 1])
	D[3 * n + 2] = min(n, D[3 * n + 2])

# Solução

# Rodadas
n = int(input())

# Pontuações
o = 0
e = 0
i = 0

# Para cada rodada
for _ in range(n):
	# Jogador inicial e valor inicial
	c, k = input().split(' ')
	k = int(k)

	# Apenas somamos o valor da tabela que já foi calculado
	# Levando em conta a ordem das jogadas
	if c == 'O':
		o += D[3 * k + 0]
		e += D[3 * k + 1]
		i += D[3 * k + 2]
	elif c == 'E':
		e += D[3 * k + 0]
		i += D[3 * k + 1]
		o += D[3 * k + 2]
	else:
		i += D[3 * k + 0]
		o += D[3 * k + 1]
		e += D[3 * k + 2]

print(o, e, i)