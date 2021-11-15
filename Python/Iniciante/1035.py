# Problema 1035 - Beecrowd - Iniciante - Nível 2

# Vamos ler os valores como inteiros
a, b, c, d = map(int, input().split())

# E fazer todas as verificações que o problema pede
if b > c and d > a and (c+d) > (a+b) and c > 0 and d > 0 and a%2==0:
	print('Valores nao aceitos')
else:
	print('Valores aceitos')