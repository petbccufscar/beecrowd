# Problema 2750 - URI - Iniciante - Nível 1

# Impressão do cabeçalho da tabela
print("---------------------------------------")
print("|  decimal  |  octal  |  Hexadecimal  |")
print("---------------------------------------")

# FOR responsável pela impressão da tabela formatada
# ':^N' alinha a variável de forma centralizada ocupando N casas.
for i in range(0, 16):
	# String com a representação em hexadecimal
	# A função 'hex' retorna uma string que começa com '0x', quem não será usada
	h = hex(i).replace('0x', '').upper()
	
	# String com a representação em octal
	# A função 'oct' retorna uma string que começa com '0o', quem não será usada
	o = oct(i).replace('0o', '')

	print(f'|  {i:^9}|{o:^9}|{h:^15}|')

# Impressão do rodapé da tabela
print("---------------------------------------")