# Problema 2310 - Beecrowd - Iniciante - Nível 2

# Número de jogadores
n = int(input())

# Temos duas listas que vão guardar o total de
# tentativas e sucessos de todos os jogadores
# Para cada lista temos 3 valores, S, B e A
total_tentativas = [0] * 3
total_sucessos = [0] * 3 

# Para cada jogador
for i in range(n):
    # Vamos receber e ignorar o nome do jogador
    input()

    # Recebendo tentativas
    # Dividimos a entrada em uma lista, que convertemos (mapeamos) para números (integers/int)
    # A função zip() vai juntar o S recebido com o S do total, o B recebido com o B total...
    # Ex:
    #  tentativas (input do usuário) = (1, 2, 3)
    #  total_tentativas = (7, 8, 9)
    #  zip(tentativas, total_tentativas) = ((1, 7), (2, 8), (3, 9)) 
    # Usamos uma "compreensão de lista" pra gerar uma lista somando cada item
    # Ex:
    #                                          x+y, x+y, x+y
    #  Continuando o último, o nosso zip vira (1+7, 2+8, 3+9) = (8, 10, 12)
    # Essa nova lista vira o total de tentativas
    tentativas = map(int, input().split())
    total_tentativas = [x + y for x, y in zip(tentativas, total_tentativas)]

    # Recebendo sucessos
    # Fazemos a mesma coisa para o número de sucessos
    sucessos = map(int, input().split())
    total_sucessos = [x + y for x, y in zip(sucessos, total_sucessos)]

# Ao final do loop temos o total, vamos usar a mesma técnica para calcular
# as porcentagens
porcentagens = [s / t for s, t in zip(total_sucessos, total_tentativas)]

# Agora imprimimos no formato adequado
# (Com porcentagem e duas casas após o ponto)
print(f"Pontos de Saque: {porcentagens[0]*100:.2f} %.")
print(f"Pontos de Bloqueio: {porcentagens[1]*100:.2f} %.") 
print(f"Pontos de Ataque: {porcentagens[2]*100:.2f} %.")

# Alternativa caso não precisasse de um espaço entre o número e o '%'
# print(f"Pontos de Saque: {porcentagens[0]:.2%}.")
