# Leitura de quantos casos serão feitos
t = int(input())

# Realiza T casos de teste
for i in range(t):

	# Quantos Nomes e Frequências serão lidas
	n = int(input())

	reprovados = []

	nomes = input()
	nomes = nomes.split()

	frequencia = input()
	frequencia = frequencia.split()
	
	# Verifica quais são os caracteres de cada posição do vetor frequencia, contabilizando-os
	for x in range(n):
		p=0 
		a=0
		m=0
		# Verifica o tamanho de cada string de presença/ausência 
		tam=len(frequencia[x])
	
		# Em cada posição da string e presença/ausência, verifica qual é seu caractere
		for y in range(tam):
			if frequencia[x][y] == 'P':
				p+=1

			elif frequencia[x][y] == 'A':
				a+=1
			
			# Caracter igual à 'M'
			else:
				m+=1

		# Cálculo da frequência, caso for inferir há 75% o aluno pe adicionado a lista dos reprovados
		if((p/(tam-m))<0.75):
			reprovados.append(nomes[x])
	
	# Imprimindo os reprovados no formato pedido (separados por espaço) 
	print(*reprovados)

