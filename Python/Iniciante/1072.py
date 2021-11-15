# Problema 1072 - Beecrowd - Iniciante - Nível 1

# Leitura do valore de n
n = int(input())

# Contador para os números dentro do intervalo
#   Usando 'in_' pois 'in' é uma palavra reservada
in_ = 0

# Contador para os números fora do intervalo
out = 0

# Loop para cada valor
for i in range(n):
    # Leitura do valor
    x = int(input())

    # Verificação
    if 10 <= x <= 20:
        in_ += 1
    else:
        out += 1

# Saída apresentando os valores
print(f'{in_} in')
print(f'{out} out')