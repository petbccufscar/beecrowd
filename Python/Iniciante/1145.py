# Problema 1145 - Beecrowd - Iniciante - Nível 2

# Leitura dos dois valores X e Y
# Split divide a string recebida "X Y" em "X" e "Y"
# Como o resultado de split é uma lista de strings, 
# precisamos mapear (map) cada valor para um inteiro
X, Y = map(int, input().split())

# Vamos continuar imprimindo até chegar em Y
# Precisamos do +1 no range pois ele por padrão 
# é exclusivo, não retornando seu valor final
for i in range(1, Y+1):
    # Imprimimos o número, após isso definimos se vamos
    # para a próxima linha ou acrescentamos um espaço
    print(i, end="")

    # Note que o último número de cada linha é sempre o 
    # próximo múltiplo de X. Podemos verificar se um número
    # é múltiplo de X com a operação % X 
    # (retorna o resto da divisão por X, checamos por resto = 0)
    if (i % X == 0):
        # Print de uma nova linha (Equivalente ao Enter ou \n)
        print()
    else:
        # Print de um espaço
        print(end=" ")

