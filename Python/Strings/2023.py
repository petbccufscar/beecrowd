# Problema 2023 - Beecrowd - Strings - Nível 4

nomes = []

while True:
    try:
        nomes.append(input())
    except EOFError:
        break

ultima = nomes[0]

# Seleciona o nome de "maior valor", ou seja
# aquele que em ordem alfabética ficaria por último
for i in range(len(nomes)):
    if ultima.lower() < nomes[i].lower():
        ultima = nomes[i]

print(ultima)
