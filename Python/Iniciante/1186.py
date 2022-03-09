# Problema 1186 - Beecrowd - Iniciante - Nível 3

# Iniciamos a matriz, que será uma lista de listas, a soma 
# se iniciará com 0 e recebmos a operação a ser realizade
matriz = []
soma = 0
operacao = input()

# Preenchemos a cada linha e depois, utilizamos 'append'
# para inserir a linha na matriz
for _ in range(12):
    linha = []
    for _ in range(12):
        linha.append(float(input()))
    matriz.append(linha)

# Percorremos a matriz, e quando a soma da linha com a coluna
# for maior que 11, representa que o elemento está na 
# diagonal inferior e então, é adicionado a variável SOMA
for i in range(12):
    for j in range(12):
        if (i + j) > 11:
            soma += matriz[i][j]

# De acordo com a operação, o resultado é exibido com apenas uma
# casa decimal
if operacao == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/66:.1f}')