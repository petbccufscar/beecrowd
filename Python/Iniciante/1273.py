# Problema 1273 - URI - Iniciante - Nível 3

# Quantidade de palavras na primeira iteração
quantidadePalavras = int(input())

while quantidadePalavras != 0:
    # Palavras que serão justificadas
    palavras = []

    # Número de caracteres da maior palavra
    maiorPalavra = 0

    # Recebe as palavras na entrada padrão
    for i in range(quantidadePalavras):
        palavras.append(input())

        # Atualiza a quantidade de caracteres da maior palavra
        if len(palavras[i]) > maiorPalavra:
            maiorPalavra = len(palavras[i])

    for i in palavras:
        # Espaços necessários para justificar a palavra
        espacos = " "*(maiorPalavra - len(i))
        print(espacos + i)

    quantidadePalavras = int(input())
