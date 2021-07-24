# Problema 3253 - URI - Iniciante - Nível 1

# Leitura do total de ruas
nro_ruas = int(input())

# Variável que verifica se houve algum problema
no_problem = True

# Em ruas adjacentes, guardaremos em uma chave k, os ids das ruas que são possiveis acessar diretamente por k
ruas_adjacentes = {}

# Em chegam, guardaremos em uma chave k, os ids das ruas que vão para k
chegam = {}

# Armazena a ordem em que os dados foram inseridos
# Será importante posteriormente, pois devemos imprimir o resultado na mesma ordem
id_input_order = []


# Leitura de cada rua e seus caminhos
for rua in range(nro_ruas):
    # Leitura das variáveis
    id, nro_alcancaveis, *alcancaveis = map(int, input().split(' '))

    # Adiciona na lista para guardar a ordem de entrada
    id_input_order.append(id)

    # Adiciona as ruas alcançáveis diretamente pela rua id
    ruas_adjacentes[id] = alcancaveis
    
    # Adiciona em cada rua de alcançáveis que é possível acessar pela rua id
    for i in alcancaveis:
        # Se ainda não tiver certa chave no Dicionário, será criada uma lista vazia
        if chegam.get(i) == None:
            chegam[i] = []

        # Adiciona na lista o id da rua que é possivel aceessar i
        chegam[i].append(id)
       
            
# Algoritmo de busca em profundidade (depth first search)
# Ele expande os nós de um grafo, adiciona os nós adjacentes na pilha para visitar
# E visita o último adicionado
# O vetor é o vetor de adjacência
def dfs(vetor):

    # Pilha de ruas para serem visitadas
    pilha = [0]
    
    # Lista de ruas visitadas: Verdadeiro e Falso
   
    visited = [False] * 1000

    # Enquanto houver ruas na pilha
    while pilha:
        # As ruas serão visitadas
        visited[pilha[0]] = True

        # Retiradas da pilha
        aux = pilha[0]
        pilha.pop(0)

        # Caso façam referencia (chegam em/saem de) uma rua
        # (Depende do vetor de adjacencia)
        if vetor.get(aux) != None:
            # Ele adicionará as ruas ligadas através do vetor na pilha para 
            # serem visitadas caso não tenham sido
            for rua in vetor[aux]:
                if visited[rua] == False:
                    pilha.insert(0, rua)

    # Retorna a lista de visitados
    return visited

# Utiliza o DFS para marcar as ruas que são possiveis acessar a partir da rua 0
visited = dfs(ruas_adjacentes)

# Utiliza o DFS para marcar as ruas que são possiveis chegar na rua 0
visited2 = dfs(chegam)

# Acumula as saidas para serem impressas separadamente no final 
unreachables = ''
trappeds = ''

# Percorre as ruas na ordem em que foram inseridas
for id in id_input_order:

    # Verifica se a foi possível acessar a rua 0 a partir da rua atual.
    rua = visited2[id]
    if rua == False:
        no_problem = False
        trappeds += f'TRAPPED {id}\n'

    # Verifica se a foi possível acessar a rua atual a partir da rua 0.
    rua = visited[id]
    if rua == False:
        no_problem = False
        unreachables += f'UNREACHABLE {id}\n'


# Imprime o resultado final
if no_problem:
    print('NO PROBLEMS')
else:
    # Imprime os Erros, retirando a quebra de linha desnecessária
    print(trappeds + unreachables, end='')
