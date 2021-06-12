# Problema 1017 - URI - Iniciante - Nível 1

# Lê as entradas e as armazena
time = int(input())
speed = int(input()) 

# Imprime na tela a quantidade de litros
# Dado a fórmula (Km/h * h) / Km/L
print(f'{((time*speed)/12):.3f}')