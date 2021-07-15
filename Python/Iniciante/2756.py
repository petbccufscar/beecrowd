# Problema 2756 - URI - Iniciante - Nível 1

# Colocando em variáveis linha, cada print que será necessário
linhaA = "       A"
linhaB = "      B B"
linhaC = "     C   C"
linhaD = "    D     D"
linhaE = "   E       E"

# Colocando em uma lista as linhas em ordem
listLinhas = [linhaA, linhaB, linhaC, linhaD, linhaE]

# Apresentando linha por linha, fazendo um loop com a lista, passando do começo ao final e ao contrário quando passed é true
i = 0
passed = False
while(i>=0):
  print(listLinhas[i])
  if(i==len(listLinhas)-1):
    passed = True 
  if(passed==True):
    i -= 1 
  else:
    i += 1
