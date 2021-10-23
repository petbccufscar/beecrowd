# Problema 1010 - URI - Iniciante - Nível 3

# Como todos os valores estão na mesma linha
# Lemos a linha com o 'input'
# Dividimos os valores com 'split'
# Convertemos os valores com 'map' e 'float'
# Como são três valores, cada variável recebera um
codigoA, quantidadeA, valorA = map(float, input().split())
codigoB, quantidadeB, valorB = map(float, input().split())

# Então calculamos o custo
custoA = quantidadeA * valorA
custoB = quantidadeB * valorB

# E printamos o valor formatado, com duas casas decimais
print(f'VALOR A PAGAR: R$ {(custoA + custoB):.2f}')