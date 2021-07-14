# Problema 1957 - URI - Iniciante - Nível 1

# Recebendo um número inteiro na base 10
num = int(input())

# Transformando o número em hexadecimal com a função, "hex(numero)" e armazenando na variável numHex
numHex = hex(num)

# Porém o valor da função "hex()" retorna com o prefixo da base hexadecimal "0x..." e em letras minúsculas, assim usaremos a função "split()" com parámetros "0x" para separar a resposta final e selecionaremos a parte com índice 1, pois é a nossa resposta e a função "upper()" para deixar as letras em maíusculas, como está nas respostas esperadas.
numHex = numHex.split("0x")
numHex = numHex[1]
numHex = numHex.upper()

# Exibindo o numHex
print(numHex)