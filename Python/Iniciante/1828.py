# Problema 1828 - Beecrowd - Iniciante - Nível 4

# Definindo a quantidade de casos de teste
T = int(input())

for caso in range(T):

    # Recebendo as escolhas realizadas pelos jogadores
    escolhas = [x for x in input().split(" ")]

    # Definindo todas as combinações possíveis de vitória para Sheldon
    vitoria = [
        ["tesoura", "papel"],
        ["papel", "pedra"],
        ["pedra", "lagarto"],
        ["lagarto", "Spock"],
        ["Spock", "tesoura"],
        ["tesoura", "lagarto"],
        ["lagarto", "papel"],
        ["papel", "Spock"],
        ["Spock", "pedra"],
        ["pedra", "tesoura"]
    ]

    # Definindo condição de empate
    empate = escolhas[0] == escolhas[1]

    # Imprimindo as reações de Sheldon para todos os resultados possíveis do jogo
    if escolhas in vitoria:
        print(f"Caso #{caso+1}: Bazinga!")
    elif empate:
        print(f"Caso #{caso+1}: De novo!")
    else:
        print(f"Caso #{caso+1}: Raj trapaceou!")
