# Problema 2756 - URI - Iniciante - Nível 1

# Colocando em variáveis linha, cada print que será necessário
linhaA = "       A"
linhaB = "      B B"
linhaC = "     C   C"
linhaD = "    D     D"
linhaE = "   E       E"

# Colocando em uma lista as linhas em ordem
listLinhas = [linhaA, linhaB, linhaC, linhaD, linhaE]

# Apresentando linha por linha, fazendo um loop com a lista do início ao fim
for i in range(5):
    print(listLinhas[i])
# Apresentando linha por linha, do final ao início.
for j in range(3, -1, -1):
    print(listLinhas[j])
