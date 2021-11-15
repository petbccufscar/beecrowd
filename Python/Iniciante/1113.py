# Problema 1113 - Beecrowd - Iniciante - Nível 1

# Inicializa x e y com valores diferentes
x, y = 0, 1

# Loop lendo as entradas até serem iguais
while x != y:
    # Leitura de multiplas variáveis em uma linha
    x, y = map(int, input().split(' '))
    # Caso x e y forem iguais, não haverá print
    if x != y:
        # Imprime Crescente se crescente e Decrescente caso contrário
        print("Crescente" if x < y else "Decrescente")