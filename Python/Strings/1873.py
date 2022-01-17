# Problema 1873 - Beecrowd - Strings - Nível 2

# Criação de um dict em que a chave é uma opção de arma, e seus valores são as armas que a chave ganha.
armaGanhadora = {
    "tesoura": ["papel", "lagarto"],
    "papel": ["pedra", "spock"],
    "pedra": ["lagarto", "tesoura"],
    "lagarto": ["spock", "papel"],
    "spock": ["tesoura", "pedra"],
}

# Recebendo o número de casos teste.
numCasos = int(input())


for i in range(numCasos):

    # Recebendo as armas do Rajesh e Sheldon, respectivamente.
    armaRajesh, armaSheldon = map(str, input().split(" "))

    # Verificando os casos:
    #
    #   - Se as armas são iguais primeiro.
    #   - Se não, consulte no dict se a arma do Rajesh ganha da arma do Sheldon, usando o atributo ".count"
    #   de listas que retorna quantas ocorrências tem o parâmetro passado. Caso retorne 0, então sabemos que
    #   o Sheldon venceu, pois a arma do Rajesh não ganha da dele.
    #
    # E já apresenta o resultado do jogo.
    if armaSheldon == armaRajesh:
        print("empate")
    elif armaGanhadora[armaRajesh].count(armaSheldon) == 0:
        print("sheldon")
    else:
        print("rajesh")
