# Problema 1188 - Beecrowd - Iniciante - Nível 1

# Leitura da operação
o = input()

# A matriz é uma lista de lista, iniciamos como lista vazia
m = []

for _ in range(12):
    # Colocamos uma lista vazia referente a uma linha
    m.append([])
    for _ in range(12):
        # Leitura do valor
        v = float(input())
        # Colocamos o valor na última linha da matriz
        m[-1].append(v)

# Contador de valores únicos somados
k = 0
# Soma total
soma = 0

# Loop para soma
for i in range(12):
    for j in range(12):
        # Verificamos se o valor está na área indicada
        if (11 - i) < j < i:
            # Incrementamos o contador e a soma total
            k += 1
            soma += m[i][j] 

# Aplicamos a operação
if o == 'M':
    resultado = soma/k
elif o == 'S':
    resultado = soma

# E mostramos o resultado
print(f'{resultado:.1f}')
