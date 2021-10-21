# Problema 1120 - URI - Strings - Nível 5

# Inicializamos as variáveis, pois não existe Do While em python
d = ''
n = ''

while d != '0' and n != '0':
    # Leitura das entradas
    d, n = input().split(' ')

    # Nova variável para não perder o valor inicial de n
    result = n

    # Caso não seja o fim dos casos teste:
    if d != '0' and n != '0':

        # Removendo o digito d da string result
        result = result.replace(d,'')

        # Removendo zeros a esquerda
        while len(result) > 0 and result[0] == '0':
            # Metodo de substring que começa no segundo char e vai até o fim da string
            result = result[1:len(result)]

        # Caso a string tenha ficado vazia, atribuimos 0 a ela
        if len(result) == 0:
            result = '0'
        
        # Impressão do resultado
        print(result)