# Problema 1858 - Beecrowd - Iniciante - Nível 2

# Não necessitamos da primeira entrada, que refere-se à quantidade
# de pessoas. Utilizamos '_' para sinalizar isso.
_ = int(input())

# Recebendo os inteiros que representam a quantidade de punições recebidas por Theon ao escolher uma determinada pessoa
consequencias = [int(x) for x in input().split()]

# Recebendo o índice do elemento de menor valor da lista de consequências
# Adiciona-se 1 já que o índice da lista inicia em 0
minimo = consequencias.index(min(consequencias)) + 1

# Imprimindo na tela o valor mínimo
print(minimo)
