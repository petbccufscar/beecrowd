# Recebe a quantidade de casos teste
T = int(input())

# Laço de repetição que irá executar o loop
# 3 vezes, recebendo a quantidade de garrafas
# compradas e quantidade de garrafas vazias
# para poder usufruir da promoção
for i in range(T):
    N, K = [int(i) for i in input().split()]

    # Imprime o resto da divisão de N por K
    # que indica a quantia de garrafas que sobram;
    # somando-se o valor da quantidade de garrafas
    # que efetivamente ativam a promoção dividido pelo
    # número de garrafas necessárias para ganhar uma garrafa
    print(int(N%K + (N - N%K)/K))
