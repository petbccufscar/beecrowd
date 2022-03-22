# Problema 2815 - Beecrowd - String - Nível 2

# Lê a frase e guarda como uma lista de palavras
frase = input().split(' ')

# Inicia a nova frase
novaFrase = ""

# Verifica palavra por palavra
for palavra in frase:

    # Se a palavra for maior que três e as duas primeiras letras estiverem 
    # repetidas, a palavra será reescrita corretamente
    if len(palavra) > 3 and palavra[:1] == palavra[2:3]:
        novaPalavra = palavra[2:]
    # Caso contrário, será escrito do mesmo jeito que veio
    else:
        novaPalavra = palavra

    # Adiciona a palavra corrigida na novaFrase
    novaFrase += " " + novaPalavra

# Printa o resultado final, desconsiderando o espaço inicial
print(novaFrase[1:])