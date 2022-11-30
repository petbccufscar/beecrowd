# Problema 1183 - Beecrowd - Iniciante - Nível 4

# Leitura de um caractere maiúsculo que especifica a operação
op = input()

# Leitura e Construção da matriz M[12][12]
M = [[float(input()) for x in range(12)] for y in range(12)]

# Soma total
soma = 0

# Variável auxiliar para limitar o acesso a somente colunas que
# possuem elementos acima da diagonal principal
aux = 1

# Cálculo da soma dos elementos acima da diagonal principal
for i in range(11):
    
    # A função "sum()" soma todos os valores de um objeto iterável, então
    # estamos passando a linha "i", começando do valor "aux" até o seu fim.
    soma += sum(M[i][aux:])
    aux += 1

# Aplicando a operação desejada
if op.upper() == "S":
    print(f'{soma:.1f}')
elif op.upper() == "M":
    # Como o tamanho da matriz é fixo, o número de elementos acima da
    # diagonal principal também é fixo e igual a 66
    qtd_denominadores = 66
    
    # Cálculo da média dos elementos acima da diagonal principal
    media = soma / qtd_denominadores
    print(f'{media:.1f}')