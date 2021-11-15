# Problema 2787 - Beecrowd - Iniciante - Nível 1

# Leitura das variáveis de entrada
L = int(input())
C = int(input())

# Verificando os casos baseado nas entradas serem par ou ímpar, e printando o resultado
if(L%2 == 0):
	if(C%2 == 0):
		print(1)
	else:
		print(0)
else:
	if(C%2 == 0):
		print(0)
	else:
		print(1)
