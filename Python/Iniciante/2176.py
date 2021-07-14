# Problema 2176 - URI - Iniciante - Nível 1
# Problema 2176 - URI - Iniciante - Nível 1
# Inicializa a string contendo mensagem S
S = input()

# Variável para contar a quantidade de dígitos 1
digitos = 0

# Verifica se a quantidade de dígitos
# com valor igual a 1 é par ou não
for i in S:
    if i == "1":
        digitos += 1

# Verifica se a quantidade de dígitos é par,
# testando se é divisível por 2, ou não,
# e em seguida imprimindo a mensagem
if digitos%2 == 0:
    print(S + "0")
else:
    print(S + "1")
