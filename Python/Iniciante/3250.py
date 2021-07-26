# Problema 3250 - URI - Iniciante - Nível 1

# Leitura dos valores
andares, começo, fim, cima, baixo = map(int, input().split())

# Se tivermos que descer, vamos modificar o problema
# Todos os casos passarão a ser de subida
if fim < começo:
	cima, baixo = baixo, cima
	começo      = andares - começo
	fim         = andares - fim

# Se não pudermos subir temos que usar as escadas
if cima == 0:
	print('use the stairs')
	exit()

# Calculamos quantos andares temos que subir
diferença = fim - começo

# Se a diferença for zero, chegamos
if diferença == 0:
	print(0)
	exit()

# Quantidade de vezes que subimos e descemos
u = 0
d = 0

# Vamos usar divisão e módulo para calcular quantas vezes vamos subir e descer

# Usamos a divisão inteira para subir
u += diferença//cima
# Pode ser que ainda falte alguns andares, menos que 'cima'
diferença %= cima

# Pode ser que chegamos, verificamos isso
if diferença == 0:
	print(u)
	exit()

# Se chegamos a essa parte do código
# Ainda faltam alguns andares

# Vamos subir mais uma vez, passando do 'fim'
u += 1
diferença -= cima
# Como a 'diferença' era menos que 'cima'
# Multiplicamos por '-1' para que ela volte a ser positiva
diferença *= -1

# A partir desse ponto vamos precisar ir para baixo

# Verificamos se isso é possível
if baixo == 0:
	print('use the stairs')
	exit()

# Do mesmo modo vamos usar divisão inteira para descer
d += diferença//baixo
# Pode ser que ainda falte alguns andares, menos que 'baixo'
diferença %= baixo

# Não precisamos subir ou descer novamente:
#   A 'diferença' não é multiplo de 'cima', por conta do módulo anterior
#   A 'diferença' não é multiplo de 'baixo', por conta do módulo anterior
#   Se a 'diferença' não for zero, temos um número que não pode ser dividido por 'cima' e 'baixo'

# Por fim mais uma verificação

# Se chegamos ao fim printamos a soma do número de vezes que subimos e descemos
if diferença == 0:
	print(u + d)
# Se não usamos as escadas
else:
	print('use the stairs')