# Problema 2311 - Beecrowd - Iniciante - Nível 2


# Recebe o número de pessoas
competidores = int(input())

# Inicia a lista vazia
nome = []

# Percorre o loop até chegar na quantidade total de competidores
for i in range(competidores):

    # Atribui o nome do competidor a lista vazia
    nome.append(input())

    # Recebe a dificuldade da tarefa
    dificuldade = float(input())

    # Mapeia a quantidade de notas transformando em uma lista
    notas = list(map(float, input().split()))

    # Anota o mínimo e o máximo da lista
    minimo = min(notas)
    maximo = max(notas)

    # Faz a conta e imprime o resultado com 2 casas
    nota_final = (sum(notas)-maximo-minimo)*dificuldade
    print(f'{nome[i]} {nota_final:.2f}')