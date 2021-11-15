# Problema 1038 - Beecrowd - Iniciante - Nível 1

# Entrada de dados com a função split e map para dividir os valores de entrada pelo 'espaço' e converte-los para float, respectivamente
item, qtd_item = map(float, input().split(' ')) 

# Estrutura condicional para escolher qual será o preço total cobrado.
if (item == 1):
    preco_total = 4.00*qtd_item
elif (item == 2):
    preco_total = 4.50*qtd_item
elif (item == 3):
    preco_total = 5.00*qtd_item
elif (item == 4):
    preco_total = 2.00*qtd_item
elif (item == 5):
    preco_total = 1.50*qtd_item

# Saída de dados
print(f"Total: R$ {preco_total:.2f}")
