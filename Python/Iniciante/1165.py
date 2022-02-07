# Problema 1165 - Beecrowd - Iniciante - Nível 2

# Números de testes.
numTestes = int(input())

# Loop para testar cada entrada do usuário.
for i in range(numTestes):
    num = int(input())

    # Variável booleana para teste de número primo.
    primo = True

    # Testar de método bruto para número primo.
    for aux in range(2, num):

        # Se ele foi dividido por qualquer número entre 2 e num - 1 então ele não é primo.
        if num % aux == 0:
            print(f"{num} nao eh primo")
            primo = False
            break

    # Teste da variável booleana.
    if primo:
        print(f"{num} eh primo")
