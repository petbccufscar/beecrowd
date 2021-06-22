# Problema 2029 - URI - Iniciante - Nível 1

# Declarando uma constante pi para cálculos, um vetor que armazenará os dados de área e altura para saída
pi = 3.14
area = []
altura = []

# Variável auxiliar para indice
index = 0

# Processando os dados até o EOF
while(True):
    try:
        volume_produzido = float(input())
        diametro = float(input())

        # Calculo da área da boca do recipiente
        area.append(pi*(diametro/2)**2)

        # Calculo da altura usando a área da boca do recipiente
        altura.append(volume_produzido/area[index])

        # Atualização da variável index
        index += 1
    except EOFError:
        break

# Saída de dados passando por todos os valores das listas altura e area
for i in range(len(altura)):
    print(f"ALTURA = {altura[i]:.2f}\nAREA = {area[i]:.2f}")