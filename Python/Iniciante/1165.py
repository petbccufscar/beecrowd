# Problema 1165 - Beecrowd - Iniciante - Nível 2

# Entrada de número de testes.
numTestes = int(input())

# Loop para receber os números para teste.
for i in range(numTestes):

    num = int(input())

    # Variável booleana para testar se é número primo.
    primo = True

    # Teste de método bruto para ver se um número é primo.
    for aux in range(2, num):

        # Se ele for divido por qualquer número entre 2 e num - 1, então
        # ele não é primo.
        if num % aux == 0:
            print(f"{num} nao eh primo")
            primo = False
            break

    if primo:
        print(f"{num} eh primo")
