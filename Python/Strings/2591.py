# Problema 2591 - Beecrowd - String - Nível 1

# Lendo a quantidade de testes
n = int(input())

# Percorrendo os testes
for i in range(n):
    # Lendo o hamekame e dividindo no meio 'mek'
    hamekame = input().split('mek')

    # Separando em variáveis para ficar mais facil entender
    ha = hamekame[0]
    ame = hamekame[1]

    # A quantidade de 'a' da finalização é a quantidade 
    # de 'a' na variável 'ha' vezes a quantidade de 'a' na variável 'ame'.
    aaa = ha.count('a') * ame.count('a')

    # Em python podemos multiplicar uma string por um número
    print('k' + 'a'*aaa)