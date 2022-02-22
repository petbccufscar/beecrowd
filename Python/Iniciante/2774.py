# Problema 2774 - Beecrowd - Iniciante - Nível 4

# Leitura até o fim do arquivo
while True:
    try:
        # Leitura da linha inutilizável
        _ = input()

        # Leitura da lista de valores
        sensor = list(map(float, input().split(' ')))

        # Cálculo da média dos valores
        media = sum(sensor) / len(sensor)

        # Iniciando a soma dos quadrados das diferenças como 0
        soma = 0

        # Fazendo o somatório
        for i in sensor:
            soma += (i - media) ** 2
        
        # Calculando e Imprimindo a raiz da fração com precisão .5f
        print(f'{(soma/(len(sensor)-1))**(0.5):.5f}')

    # Caso chegue no fim do arquivo (EOF), o loop para
    except EOFError:
        break

