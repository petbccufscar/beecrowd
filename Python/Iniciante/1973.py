# Problema 1973 - Beecrowd - Iniciante - Nível 7

# Leitura da entrada que corresponde ao número de Estrelas
N = int(input())

# Leitura da quantidade de carneiros por estrela e armazenando os valores separadamente em um lista
carneiros = [int(x) for x in input().split()]

# Contador de estrelas atacadas
quantidade_estrelas_atacadas = 0

# Varíavel de controle que determina qual a próxima estrela a ser atacada pelo ladrão
localizacao_ladrao = 0

# Lista que determina quais estrelas foram atacadas. Todas iniciam com o valor False, já que não foram atacadas ainda
estrelas_atacadas = [False] * N

# Loop responsável pela execução dos roubos do ladrão
# O ladrão continua roubando carneiros até que não exista a próxima estrela a ser visitada
while 0 <= localizacao_ladrao < N:

    # Determinando se a quantidade de carneiros da estrela, inicialmente, é par, ou ímpar
    qtd_carneiros_par = carneiros[localizacao_ladrao] % 2 == 0

    # Efetuando roubo do ladrão (somente quando a quantidade de carneiros é positiva)
    if carneiros[localizacao_ladrao] > 0:
        carneiros[localizacao_ladrao] -= 1

        # Caso a estrela não tenha sido atacada, definir que a estrela foi atacada
        # E incrementar a quantidade de estrelas atacadas
        if estrelas_atacadas[localizacao_ladrao] == False:
            estrelas_atacadas[localizacao_ladrao] = True
            quantidade_estrelas_atacadas += 1

    # Definindo o próxima estrela a ser atacada pelo ladrão
    # Se for par, o ladrão vai para a estrela à esquerda
    # Caso contrário, vai para a estrela à direita
    if qtd_carneiros_par:
        localizacao_ladrao -= 1
    else:
        localizacao_ladrao += 1

# Após a saída do loop, podemos somar a quantidade de carneiros restantes
total_carneiros_nao_roubados = sum(carneiros)

# Imprimindo na tela a quantidade de estrela atacadas e o total de carneiros não roubados
print(quantidade_estrelas_atacadas, total_carneiros_nao_roubados)
