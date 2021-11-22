# Problema 2763 - Beecrowd - Iniciante - Nível 1

# Entrada de dados CPF no formato: XXX.YYY.ZZZ-DD
cpf = input()

# Separando os valores da saída
cpf_separado = cpf.split(".")

# Separando os dígitos da última parte do CPF, 
# O método "extend" adiciona mais de um item na lista, deixando-os separados
# Porém é necessário remover a parte não separada com o método pop(indice)
cpf_separado.extend(cpf_separado[len(cpf_separado)-1].split("-"))
cpf_separado.pop(-3)

# Apresentando a saída
for i in cpf_separado:
    print(f"{i}")