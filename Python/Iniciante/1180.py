# Problema 1180 - Beecrowd - Iniciante - Nível 3

# Lendo a variável inicial 'n' (tamanho do vetor)
n = int(input())

# Lendo os elementos do vetor como uma string
vetor = input()

# Utilizando a função 'split' para separar cada número da string em uma posição do vetor
vetor = vetor.split()

# Transformando cada número que está como tipo de dado string em int, tendo como retorno um objeto do tipo 'map'
vetor = map(int, vetor)

# Transformando o objeto 'map' em lista novamente
vetor = list(vetor)

# Encontrando o menor valor do vetor
menor = min(vetor)

# Encontrando a posição do menor elemento do vetor
posicao = vetor.index(menor)

# Imprimindo o resultado
print(f'Menor valor:', menor)
print(f'Posicao:', posicao)