# Problema 3147 - URI - Iniciante - Nível 1

# Lendo as variáveis de entrada
H,E,A,O,W,X= map(int, input().split(' '))

# Realizando a soma dos exércitos do bem e do mal. Caso o exército do bem seja maior ou igual ao exercito do mal, Middle-earth estará salva
if(H+E+A+X) >= (O+W):
	print(f'Middle-earth is safe.')

# Caso contrário Sauron retornará 
else:
	print(f'Sauron has returned.')