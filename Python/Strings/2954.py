# Problema 2954 - Beecrowd - Strings - Nível 6

import re

N = int(input())
for _ in range(N):
    frase = input().lower()
    
    # Regex para encontrar as palavras jogo e perdi que não sejam substrings
    frase = frase.replace('$', '') # Removendo $
    frase = re.sub(r'[ ,.:;]*(jogo|perdi)[ ,.:;$]*', '\\1$', frase) # Marcando final das palavras jogo e perdi com $
    jogos = frase.split('$') # Dividindo frase pelo $
    # Isso permite que a divisão inclua a palavra jogo e perdi, que vão ser utilizadas
    # na contagem de segundos.

    # Removendo pontuação e espaços
    jogos = [[c for c in item if c.isalpha()] for item in jogos]

    print(len(max(jogos, key=len)))
