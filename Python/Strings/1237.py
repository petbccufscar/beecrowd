# Problema 1237 - Beecrowd - Strings - Nível 6

# Laço para ler as várias entradas.
while True:
    try:
        # Recebendo as stringsde entrada.
        string1 = input()
        string2 = input()

        # Para melhor otimização do código a string que será comparada será sempre a menor.
        if len(string1) > len(string2):
            aux = string1
            string1 = string2
            string2 = aux

        # Variável para guardar o tamanho da substring em comum entre as duas strings.
        maxSubString = 0

        # Para o problema de substrings, é necessário de 2 variáveis de início e fim
        # que irá varrer uma string, criar uma substring e verificar se na outra string possui essa substring.
        for inicio in range(len(string1)):
            for fim in range(inicio + 1, len(string1) + 1):

                # Testa se a substring está dentro da outra string e se seu tamanho é maior que o tamanho que já temos.
                if string1[inicio:fim] in string2 and maxSubString < len(string1[inicio:fim]):
                    maxSubString = len(string1[inicio:fim])

        # Apresentação da resposta
        print(maxSubString)

    except EOFError:
        break
