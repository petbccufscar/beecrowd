# Problema 2692 - Beecrowd - Strings - Nível 4

trocadas = {}

# N = Número de letras trocadas
# M = Número de frases
# "List comprehension" para converter N e M para inteiros
N, M = [int(x) for x in input().split()]

# Loop de entrada N
for _ in range(N):
    tecla1, tecla2 = input().split()
    # Colocamos a troca dentro do dicionário
    trocadas[tecla1] = tecla2
    trocadas[tecla2] = tecla1

# Loop de entrada M e troca
for _ in range(M):
    frase_alterada = input()
    frase_original = ""

    for char in frase_alterada:
        # Se devemos trocar o caractere
        if char in trocadas:
            # Adicionamos a troca na string final
            frase_original += trocadas.get(char, '')
        else:
            # Se não, colocamos o caractere mesmo
            frase_original += char

    print(frase_original)