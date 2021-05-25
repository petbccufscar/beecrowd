#Resolução problema URI 1009 - Iniciante - Nível 2
# Vitor de Almeida Recoaro - PET-BCC.
# 24/05/2021

nome = input()
salario = float(input())
total_vendas = float(input())

total_recebido = salario + (total_vendas*0.15)
print("TOTAL = R$ %.2f" %total_recebido)
