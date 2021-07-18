# Problema 3142 - URI - Iniciante - Nível 1

import sys

# Cálculo da posição da coluna para 1 letra apenas
# Usa-se a posição na tabela ASCII menos 64
def umaLetra(linha):
    return ord(linha[0])-64
# Cálculo da posição da coluna para 2 letras
# Aqui considera-se que a posição AA (27) vem após a posição Z (26)
def duasLetras(linha):
    return 26 + (ord(linha[0])-65)*26 + ord(linha[1])-64
# Cálculo da posição da coluna para 3 letras
# Aqui considera-se que a posição AAA (703) vem após a posição ZZ (26 + 26*26 = 702)
def tresLetras(linha):
    return 26 + 26*26 + 26*((ord(linha[0])-65)*26 + ord(linha[1])-65) + ord(linha[2])-64

# Laço para ler linha a linha da entrada padrão de dados
for linha in sys.stdin:
    # Se a linha possui apenas uma letra, usar função umaLetra(linha)
    if len(linha[:-1]) == 1:
        print(umaLetra(linha))
    # Se a linha possui apenas duas letras, usar função duasLetras(linha)
    elif len(linha[:-1]) == 2:
        print(duasLetras(linha))
    # Se a linha possui apenas três letras
    elif len(linha[:-1]) == 3:
        # Caso a primeira letra seja maior que X
        caso1 = linha[0] > 'X'
        # Caso a primeira letra seja X e a segunda ultrapasse F
        caso2 = linha[0] == 'X' and linha[1] > 'F'
        # Caso a primeira letra seja X, a segunda seja F e a terceira ultrapasse D
        caso3 = linha[0] == 'X' and linha[1] == 'F' and linha[2] > 'D'
        # Se for algum dos casos anteriores, a coluna não existe
        if caso1 or caso2 or caso3:
            print("Essa coluna nao existe Tobias!")
        # Caso contrário, a coluna existe, então usa-se a função tresLetras(linha)
        else:
            print(tresLetras(linha))
    # Caso a entrada tenha mais de 3 letras
    else:
        print("Essa coluna nao existe Tobias!")
