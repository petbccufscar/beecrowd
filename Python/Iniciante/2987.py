# Problema 2987 - URI - Iniciante - Nível 1

# Recebendo do usuário a entrada de uma letra maiúscula.
letra = input()

# Usando a tabela ASCII, cada caracter tem um código, podendo ser recebido pela função "ord()", e sabendo que o A tem código 65, subtraímos 64 de cada letra que teremos a posição dela.
posLetra = ord(letra) - 64

# Mostrando a posição em que a letra se encontra.
print(posLetra)