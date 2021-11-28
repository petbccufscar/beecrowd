# Problema 1273 - Beecrowd - Iniciante - Nível 3

# Quantidade de palavras na primeira iteração
quantidadePalavras = int(input())

# Flag necessário para printar as linhas entre os casos
primeiro = True

while True:
    quantidadePalavras = int(input())

    if quantidadePalavras == 0:
        break

    # Vamos printar a linha antes de cada caso, já que ela não está presente no fim
    # O primeiro caso não tem nada antes
    if primeiro:
        primeiro = False
    else:
        print()

    # Palavras que serão justificadas
    palavras = []

    # Número de caracteres da maior palavra
    maiorPalavra = 0

    # Recebe as palavras na entrada padrão
    for i in range(quantidadePalavras):
        palavra = input()
        
        palavras.append(palavra)

        # Atualiza a quantidade de caracteres da maior palavra
        maiorPalavra = max(maiorPalavra, len(palavra))

    for palavra in palavras:
        # Espaços necessários para justificar a palavra
        print(palavra.rjust(maiorPalavra))
