while True:
    n = int(input())
    if n == 0:
        break

    pontuacoes = []
    tA, tB = 0, 0

    for i in range(n):
        nome = input()
        pontuacao = sum(map(ord, nome))
        pontuacoes.append(pontuacao)
        tB += pontuacao * (i + 1)

    r = 0

    for i in range(n):
        tB -= pontuacoes[i]
        tA += pontuacoes[i]

        if tA == tB:
            r = i + 1
            break

        if tA > tB:
            break

    if r == 0:
        print("Impossibilidade de empate.")
    else:
        print(input())
