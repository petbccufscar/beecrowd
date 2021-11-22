# Problema 1050 - Beecrowd - Iniciante - Nível 2

# Recebe o ddd
ddd = int(input())

# Estado inicial da existencia do ddd no dicionário
existe = False

# Declaração do dicionário com os ddd's e seus respectivos estados
cidades = {
        61: "Brasilia", 71: "Salvador",
        11: "Sao Paulo", 21: "Rio de Janeiro",
        32: "Juiz de Fora", 19: "Campinas",
        27: "Vitoria", 31: "Belo Horizonte"
        }

# Itera sobre o dicionário em busca do ddd informado
for i in cidades:
    if i == ddd:
        print(cidades[i])
        # Indica que encontrou o ddd na lista
        existe = True
        break

if not(existe):
    print("DDD nao cadastrado")
