# lê as entradas e as armazena
time = int(input())
speed = int(input()) 

# imprime na tela a quantidade de litros
# dado a fórmula (Km/h * h) / Km/L
print(f'{((time*speed)/12):.3f}')