# Problema 1168 - Beecrowd - Strings - Nível 3

# O custo de leds para cada um dos algarismos 0~9
custo = [6,2,5,5,4,5,6,3,7,6]

# Lendo quantos casos serão lidos
loops = int(input())

for i in range(loops):
    # Lendo o número
    numero = input()
    sum = 0

    # Adicionando o custo de cada número na soma 
    for i in numero:
        sum += custo[int(i)]

    # Imprimindo o resultado
    print(f'{sum} leds')