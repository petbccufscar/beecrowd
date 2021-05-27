#Entrada de dados
nome = input() 
salario = float(input()) #Uso do caster "float" para forçar a entrada seja float
total_vendas = float(input())

#Calculo do total recebido pelo vendedor
total_recebido = salario + (total_vendas*0.15)

#Mostrando ao usuário com duas casas decimais com o "%.2f"
print("TOTAL = R$ %.2f" %total_recebido
