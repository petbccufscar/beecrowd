 # Problema 1079 - URI - Iniciante - Nível 1

#Leitura das variáveis
numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())

#Cálculo do salário
salario = horas_trabalhadas * valor_hora

#Imprimindo as saídas
print(f'NUMBER = {numero_funcionario}')
print(f'SALARY = U$ {salario:.2f}')