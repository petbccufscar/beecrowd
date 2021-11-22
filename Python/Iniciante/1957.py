# Problema 1957 - Beecrowd - Iniciante - Nível 1

# Recebendo um número inteiro na base 10
num = int(input())

# Transformando o número em hexadecimal com a função, "hex(numero)" e armazenando na variável numHex
numHex = hex(num)

# A função 'hex' retorna uma string que começa com '0x', quem não será usada.
# A função upper() deixa em letras maíusculas, como está nas respostas esperadas.
numHex = numHex.replace('0x','').upper()

# Exibindo o numHex
print(numHex)
