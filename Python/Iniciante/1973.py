# Problema 1973 - Beecrowd - Iniciante - Nível 7

# Leitura da entrada que corresponde ao número de Estrelas
N = int(input())

# Leitura da quantidade de carneiros por estrela e armazenando os valores separadamente em um lista
carneiros = list(map(int, input().split()))

# Inicializando variável responsável por decrementar o segundo roubo (volta) que seria realizado pelo ladrão
# em estrelas que possuiam, inicialmente, somente 1 carneiro
estrelas_com_um_carneiro = 0

# Inicializando variáveis resultado
total_carneiros = qtd_estrelas_atacadas = 0

# Inicializando variável de controle responsável por indicar se uma estrela com quantidade par de carneiros foi encontrada
primeira_qtd_par_encontrada = False

# A estratégia consiste em percorrer as estrelas da esquerda para a direita até encontrar uma estrela que
# possua uma quantidade de carneiros par, pois quando for encontrada uma estrela com essa característica
# o ladrão NECESSARIAMENTE irá retornar todo o seu caminho percorrido, encerrando o percurso pela esquerda. 
# Caso nenhuma das estrelas possua uma quantidade par de carneiros, o ladrão interromperá sua jornada pela direita
for index, qtd_carneiros_estrela in enumerate(carneiros):
    
    # Realizando a soma total de carneiros
    total_carneiros += qtd_carneiros_estrela
    
    if not primeira_qtd_par_encontrada:
        
        # Verificando se a quantidade de carneiros da estrela é par. Caso verdadeiro:
        # - a quantidade de estrela atacadas é dada por index + 1 (pois o índice da lista inicia-se em 0)
        # - subtrai-se a quantidade de carneiros roubados pelo ladrão do total de carneiros. Esse valor se dá
        # pela fórmula (index * 2) + 1 - estrelas_com_um_carneiro. Em que (index * 2) + 1 representa a quantidade
        # de carneiros roubados (ida + volta)
        # - setando a variável de controle primeira_qtd_par_encontrada para True a fim de que o loop for realize 
        # somente a soma dos carneiros
        if qtd_carneiros_estrela % 2 == 0:
            qtd_estrelas_atacadas = index + 1
            total_carneiros -= (index * 2) + 1 - estrelas_com_um_carneiro
            primeira_qtd_par_encontrada = True
    
        # Verificando se a estrela possui somente 1 carneiro. Caso verdadeiro:
        # incrementa a variável estrelas_com_um_carneiro
        if qtd_carneiros_estrela - 1 == 0:
            estrelas_com_um_carneiro += 1

# Caso não seja encontrada uma estrela com quantidade de carneiros par, todas as estrelas são atacadas e o total
# de carneiros é dado pela quantidade total de carneiros menos a quantidade de estrelas
if not primeira_qtd_par_encontrada:
    qtd_estrelas_atacadas = N
    total_carneiros -= N

print(qtd_estrelas_atacadas, total_carneiros)