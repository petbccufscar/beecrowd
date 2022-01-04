# Problema 1064 - Beecrowd - Iniciante - Nível 2

# Cria uma lista para os valores positivos
positivos = []

# Lerá 6 valores no teclado
for i in range(6):
    num = float(input())

    # Se for positivo, guardará na lista de positivos
    if num > 0:
        positivos.append(num)

# A função "len()" de uma lista, retorna o tamanho dela,
# logo a quantidade de números positivos que foram digitados.
# E a função "sum()" soma todos os valores dentro da lista.
# assim se dividirmos a soma dos valores, pelo seu tamanho
# temos a média, e usa-se o ".1f", para restringir a uma casa decimal.
print(f"{len(positivos)} valores positivos\n{(sum(positivos)/len(positivos)):.1f}")
