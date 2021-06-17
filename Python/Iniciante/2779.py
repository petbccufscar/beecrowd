# Problema 2779 - URI - Iniciante - Nível 1

# Entrada de dados, primeiro o número de figurinhas no álbum inteiro e segundo quantas figurinhas foram compradas
total_fig = int(input())
total_figCompradas = int(input())

# Criando um vetor auxilar para verificar se a figurinha é repetida
fig_possuidas = []

# Recebendo das figurinhas compradas, quais foram que saíram
for i in range(total_figCompradas):
    fig = int(input())

    # Verificando se a figurinha comprada não é repetida pelo método "count" que conta o tanto que um item "fig" tem no vetor
    # Assim se a figurinha não é repetida cole a figurinha diminuindo o valor do total de figurinhas restantes 
    if(fig_possuidas.count(fig)==0):
        fig_possuidas.append(fig)
        total_fig -=1

# Apresentando o total de figurinhas faltantes
print(total_fig)       