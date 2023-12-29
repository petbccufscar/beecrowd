# Recebe a quantidade de palavras (N) como um inteiro
n = int(input())

# Recebe as palavras como uma lista de strings
palavras = input().split()

# Itera sobre cada índice (i) no intervalo de 0 até n-1
for i in range(n):
    # Obtém a palavra atual
    palavra = palavras[i]
    
    # Verifica se a palavra tem exatamente 3 caracteres
    if len(palavra) == 3:
        # Verifica se a palavra começa com 'OB'
        if palavra[:2] == 'OB':
            # Substitui a palavra corrigida 'OBI' no lugar da palavra original
            palavras[i] = 'OBI'
        # Verifica se a palavra começa com 'UR'
        elif palavra[:2] == 'UR':
            # Substitui a palavra corrigida 'URI' no lugar da palavra original
            palavras[i] = 'URI'

# Imprime as palavras corrigidas, unidas por um espaço
print(' '.join(palavras))
