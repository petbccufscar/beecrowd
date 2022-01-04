# Problema 1098 - Beecrowd - Iniciante - Nível 2

# Pelo o que é possível notar, o número I da sequência será acrescido 0.2
# a cada vez que o J chegar até o número 3, e o J é a soma entre o número I
# mais a sequência 1, 2, 3.

i = 0.0
while i <= 2:
    for j in range(3):
        respostaJ = i + (j + 1)

        # No exercício é necessário que a lista distingue número inteiro de números
        # decimais, assim é necessário verificar se o I é inteiro e mostrar ele como inteiro,
        # caso contrário mostrar ele como número decimal mesmo.
        if i.is_integer():
            print(f"I={int(i)} J={int(respostaJ)}")
        else:
            print(f"I={i} J={respostaJ}")

    # A linguagem python possue um problema de precisão dos números decimais, 
    # pois ao somar 0.2 no I, em algum momento a precisão irá somas 0.2000000001, assim
    # para não ocorrer nenhum problema no exercício faço operações de soma de inteiro e
    # depois tranformo em decimal da seguinte maneira: multiplicando por 10, somo 2, e divido por 10 novamente.
    i *= 10
    i += 2
    i /= 10
