# Problema 1018 - URI - Iniciante - Nível 4

# Vamos ler o valor e converter para inteiro
valor = int(input())

# Vamos usar um vetor com os valores das notas
notas = [100, 50, 20, 10, 5, 2, 1]

# O problema requer o valor na resposta
print(valor)

# Vamos fazer um loop para calcular a quantidade de cada nota
for nota in notas:
	# Vamos ver quantas notas desse valor cabem no valor 
	quantidade = valor//nota
	# O resto passa a ser o novo valor
	valor = valor%nota
	# Então printamos a quantidade de notas
	print(f'{quantidade} nota(s) de R$ {nota},00')