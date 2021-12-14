# Problema 1080 - Beecrowd - Iniciante - Nível 2

# Declaramos a lista vazia
lista = []

# Primeiramente, lemos os 100 valores e colocamos na lista
for i in range(100):
    lista.append(int(input()))

# Mostramos o maior valor da lista e logo após, sua posição na lista
print(max(lista))
print(lista.index(max(lista)) + 1)