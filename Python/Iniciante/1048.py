# Problema 1048 - Beecrowd - Iniciante - Nível 2

# Recebe o valor na entrada padrão
salario = float(input())

# Inicializa as variáveis que serão usadas para imprimir os valores
percentual = 0
novoSalario = 0
reajuste = 0

# Verifica em qual intervalo o salário está e
# faz as devidas atribuições às variáveis
if salario <= 400:
    percentual = 0.15
elif salario <= 800:
    percentual = 0.12
elif salario <= 1200:
    percentual = 0.10
elif salario <= 2000:
    percentual = 0.07
else:
    percentual = 0.04

novoSalario = salario + salario*percentual
reajuste = salario*percentual

# Imprime os resultados obtidos com base no salário informado
print(f"Novo salario: {novoSalario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {(percentual*100):.0f} %")
