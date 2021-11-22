# Problema 1367 - Beecrowd - Strings - Nível 3

from collections import defaultdict

while True:

    # Leitura do número de submissões
    n = int(input())

    if n == 0:
        break

    # Vamos usar números complexos para contar
    # quantas submissões incorretas foram enviadas
    # A parte real será a pontuação final
    status = defaultdict(complex)

    for _ in range(n):
        # Leitura da submissão
        letra, t, julgamento = input().split()

        # O tempo precisa ser um inteiro
        t = int(t)

        if julgamento == 'correct':
            # Se a submissão estiver correta vamos
            # converter o número complexo para real
            # multiplicando por -1j, tornando o número real
            # então por 20, pela penalidade
            status[letra] *= -1j * 20
            status[letra] += t
        else:
            # Se estiver errada vamos incrementar a parte imaginária
            status[letra] += 1j

    soluções = 0
    pontuação = 0

    # Então iteramos pelos valores
    for pontos in status.values():
        # Se a parte real é positiva
        # significa que o problema teve uma submissão correta
        if pontos.real > 0:
            soluções += 1
            pontuação += int(pontos.real)

    print(f'{soluções} {pontuação}')
