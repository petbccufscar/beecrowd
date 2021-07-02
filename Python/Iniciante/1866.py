# Problema 1866 - URI - Iniciante - Nível 1

# Leitura do número de casos de teste
C = int(input())
# Laço de repetição para cada caso de teste
for i in range(C):
    # Leitura da quantidade de termos do somatório
    termos = int(input())
    # Se a quantidade total de termos do somatório for par, então o resultado
    # será igual a 0
    if termos % 2 == 0:
        print('0')
    # Caso a quantidade de termos for ímpar, o resultado será 1
    else:
        print('1')
