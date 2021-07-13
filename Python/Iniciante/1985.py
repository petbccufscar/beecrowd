# Problema 1985 - URI - Iniciante - Nível 1

# Recebemos a entrada de quantos itens diferentes foram comprados.
n = int(input())

# Valor final que será exibido é setado como 0 no início.
valor = 0.0

# Para cada compra
for i in range(n):

    # Recebemos a entrada do código do item, sua quantidade e atribuimos esses valores a variáveis com a função split()
    entrada = input()
    item, quantidade = entrada.split(' ')

    # Com uma cadeia de if's, para cada código de item, somamos ao valor total o produto da quantidade pelo respectivo valor do item.
    if int(item) == 1001:
        valor += int(quantidade) * 1.50
    elif int(item) == 1002:
        valor += int(quantidade) * 2.50
    elif int(item) == 1003:
        valor += int(quantidade) * 3.50
    elif int(item) == 1004:
        valor += int(quantidade) * 4.50
    elif int(item) == 1005:   
        valor += int(quantidade) * 5.50

# Por fim, imprimimos o valor resultante com duas casas decimais.
print('%.2f' %valor)
