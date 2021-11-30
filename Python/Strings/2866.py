# Problema 2866 - Beecrowd - Strings - Nível 2
# POR PROBLEMA DO CRIADOR DO EXERCÍCIO, NO SITE HÁ ERRO DE
# "Presentation Error" que indica que a resposta está correta,
# mas mostrada de forma errada. Então o raciocínio está certo
# para resolução do problema.

# Receber o número de casos de testes.
numTestes = int(input())

# Para cada caso teste, recebe uma string e descriptografa.
for i in range(numTestes):
    entrada = input()
    saida = ""

    # Cada letra é testada, se caso seja minúscula, adiciona na saída
    for letra in entrada:
        if letra.isupper() == False:
            saida += letra

    # Após testar a letra é necessário inverter a saída e apresentá-la
    saida = saida[::-1]
    print(saida)
