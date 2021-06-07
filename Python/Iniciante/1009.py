# Problema 1009 - URI - Iniciante - Nível 2

#Entrada de dados
#Uso do caster "float" na linha 4 e 5 para forçar a entrada seja float
nome = input() 
salario = float(input()) 
total_vendas = float(input())

#Calculo do total recebido pelo vendedor
total_recebido = salario + (total_vendas*0.15)

#Mostrando ao usuário com duas casas decimais com o ".2f"
print(f"TOTAL = R$ {total_recebido:.2f}")
