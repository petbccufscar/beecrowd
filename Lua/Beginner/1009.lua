nome = io.read("*l")
salario = io.read("*n")
vendas = io.read("*n")
salarioFinal = salario + vendas * 0.15
print(string.format('TOTAL = R$ %.2f', salarioFinal))