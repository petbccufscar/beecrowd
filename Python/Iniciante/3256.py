# Problema 3256 - Beecrowd - Iniciante - Nível 1
# Adaptado da solução original, disponível em https://nordic.icpc.io/ncpc2011/

# Leitura da quantidade de soldados e quantidade de pares de inimigos
n, m = map(int, input().split(' '))

# Lista que conterá os inimigos de k, na posição k-1 da lista 
g = []

# Criando listas vazias de inimigos para cada soldado
for i in range(n):
    g.append([])

for i in range(m):
    a,b = map(int, input().split(' '))

    # Os números que indicam os soldados começam no 1
    # Para aumentar a praticidade, subtrairemos 1 de cada número lido
    a -= 1 
    b -= 1

    # Adiciona os inimigos na lista de inimigos respectiva
    g[a].append(b)
    g[b].append(a)

# Vamos tratar esse problema como um problema de coloração de grafo
# Um exemplo simple de problema de coloração de grafos é:
# Quantas cores são necessárias para pintar os estados do mapado Brasil,
#   tal que estados adjacentes não tenha a mesma cor?
# Nesse caso, cada soldado terá sua cor, e cada um só pode ter no máximo, um inimigo da mesma cor
# Basicamente, cada cor representará um grupo.
# Como cada soldado pode ter no máximo 3 inimigos, então 2 'cores' é o máximo que nossa solução pode atingir

# Todos começam com a cor 2, como no máximo teremos 2 cores, esse valor mudará definitivamente
# Basicamente, o valor 2 é reservado para os não visitados
col = [2]*n

# Vetor de número de inimigos na mesma cor/grupo
enem = [0]*n


for i in range(n):

    # Lista com a contagem atual de inimigos com as cores 0, 1 e 2
    cnt = [0,0,0]

    # Percorre todos os inimigos de i+1
    for j in range(len(g[i])):
        # Pega a cor atual do inimigo
        index = col[g[i][j]]
        # Adiciona um no contador de inimigos por cor
        cnt[index] += 1

    # Define a cor atual do soldado para 0
    color = 0
    cur = i

    # Se a contagem de inimigos na cor 0 for maior que 1
    # Troca a cor para 1
    if cnt[0] > 1:
        color = 1

    while True:
        # Atualiza a cor do soldado atual (cur) no vetor de cores
        col[cur] = color

        # Define o último inimigo com conflitos para -1, para assim, 
        #   marcar que não há inimigo com conflito ainda
        ncur = -1

        # Percorre todos os inimigos do soldado atual
        for j in range(len(g[cur])): 

            # Se o inimigo tiver a mesma cor que o soldado atual
            if col[g[cur][j]] == color:
            
                # Acrescenta um inimigo no vetor enem na posição atual e no inimigo atual
                enem[cur] += 1
                enem[g[cur][j]] += 1

                # Se ultrapassou o limite de um inimigo por cor
                # Teremos que recalcular a cor do inimigo
                if enem[g[cur][j]] == 2:
                    
                    ncur = g[cur][j]

                    # Percorre os inimigos do inimigo atual (ncur)
                    for l in range(len(g[ncur])):

                        # Se retira da contagem
                        if col[g[ncur][l]] == color:
                        
                            enem[g[ncur][l]] -= 1
                            enem[ncur] -= 1
                        
        # Se não houveram inimigos com mais de um inimigo no grupo
        # Então o algoritmo acabou, e com isso, pode parar
        if ncur == -1:
            break

        # O soldado atual será o último inimigo que teve conflito
        cur = ncur

        # A cor do próximo começará o oposto da atual
        # Colocando assim, o soldado inimigo (ncur) numa equipe diferente do soldado atual dessa iteração
        color = 0 if color == 1 else 1

res = [[],[]]

# Adiciona os soldados em seus grupos
for i in range(n):
    res[col[i]].append(i)

# Caso tenha sido necessário usar a segunda cor: imprimir 2
# Caso contrário: imprimir 1
print(f'{2 if len(res[1]) > 0 else 1}')


# Devido alguns erros de apresentação a impressão do resultado será feita dessa forma
for i in range(2):
    for j in range(len(res[i])):
        # Será adicionado 1, pois no começo do código retiramos 1 do número do soldado
        print(res[i][j] + 1, end='')
        if (j + 1) < len(res[i]):
            print(" ", end='')
        else:
            # Imprime quebra de linha
            print()
        
