# Problema 2172 - URI - Iniciante - Nível 1
# Problema 2172 - URI - Iniciante - Nível 1
# Inicializa as variáveis e atribui
# os valores de X e EXP nessas variáveis
X, EXP = map(int, input().split(' '))

# Executa a operação de imprimir o valor de
# EXP multiplicado por X e atribui novos valores
# a essas variáveis, continuando o laço
# enquanto ambas não tiverem valor igual a 0
while X != 0 and EXP != 0:
    print(X*EXP)
    X, EXP = map(int, input().split(' '))
