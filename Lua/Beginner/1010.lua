valorTotal = 0
codigo, numero, valor = io.read('*n', '*n', '*n')
valorTotal = valorTotal + numero * valor
codigo, numero, valor = io.read('*n', '*n', '*n')
valorTotal = valorTotal + numero * valor
print(string.format('VALOR A PAGAR: R$ %.2f', valorTotal))