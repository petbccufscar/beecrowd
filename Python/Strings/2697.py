# Problema 2697 - Beecrowd - Strings - Nível 7

# Existem 3 casos diferentes que podem ser solucionados, referentes as três operações:
# Caso 1) O número de ocorrências de um inteiro é um a menos do que o esperado
# Caso 2) O número de ocorrências de um número é um a mais do que o esperado
# Caso 3) Caso 1 e 2 simultâneamente
# Se não batermos em nenhum desses, não é possível solucionar.

def try_caso3(ocorrencias):
    # Para o terceiro caso, todos os números exceto dois serão exatamente a média
    media = sum(ocorrencias.values())/len(ocorrencias)

    if media.is_integer():
        diferentes = []
        contador = 0

        for inteiro, oc in ocorrencias.items():
            if oc != media:
                contador += 1
                diferentes.append((oc, inteiro)) # Vamos ordenar pelo primeiro item depois
            if contador > 2:
                return
        
        diferentes.sort()
        print(f"-{diferentes[1][1]} +{diferentes[0][1]}")
        exit()

    else:
        return

def try_casos1_2(ocorrencias):
    ocorrencias_diferentes = []
    for inteiro, oc in ocorrencias.items():
        if not any(entry[1] == oc for entry in ocorrencias_diferentes):
            ocorrencias_diferentes.append((list(ocorrencias.values()).count(oc), oc, inteiro, ))
    
    if len(ocorrencias_diferentes) > 2:
        return
    
    ocorrencias_diferentes.sort()
    alterar = ocorrencias_diferentes[0]
    manter = ocorrencias_diferentes[1]

    if alterar[0] == 1: # Apenas um diferente
        if alterar[1]+1 ==  manter[1]:
            print(f"+{alterar[2]}")
            exit()
        elif alterar[1]-1 == manter[1]:
            print(f"-{alterar[2]}")
            exit()
        else:
            return

    # Para os casos 2 e 3, queremos encontrar o *único* inteiro com ocorrência diferente dos demais



# Mantendo um dicionário com o número de ocorrências
ocorrencias = {}

# Usando K para iniciar o dicionário com 0 em todos os valores

K, N = input().split(' ')
K = int(K)

for i in range(1, K+1):
    ocorrencias[i] = 0

# Contando ocorrências de cada inteiro
entrada = input().split(' ')
for inteiro in entrada:
    ocorrencias[int(inteiro)] += 1

# Tentando cada caso, ou retornando *
try_caso3(ocorrencias)
try_casos1_2(ocorrencias)
print("*")
