# Problema 2866 - Beecrowd - Strings - Nível 2

# Receber o número de casos de testes.
numTestes = int(input())

# Para cada caso teste, recebe uma string e descriptografa.
for i in range(numTestes):
    entrada = input()
    saida = ""

    # Cada letra é testada, se caso seja minúscula, adiciona na saída
    for letra in entrada:
        if letra.islower():
            saida += letra

    # Após testar a letra é necessário inverter a saída e apresentá-la
    saida = saida[::-1]
    print(saida)
