# Problema 1021 - Beecrowd - Iniciante - Nível 6

# Recebe o valor na entrada padrão
valor = float(input())

# Converte o valor para um número inteiro, simbolizando os centavos
valor = int(valor*100)

# Para cada cédula, calcula o resultado inteiro da divisão do valor
# por aquela cédula, armazena o resultado dessa divisão, que é o número
# de cédulas que é possível devolver sem ultrapassar o valor informado,
# e, por fim, atualiza o novo valor para o que restou após trocar parte
# do valor pela cédula que acabou de ser calculada
nota100 = valor//10000
valor %= 10000
nota50 = valor//5000
valor %= 5000
nota20 = valor//2000
valor %= 2000
nota10 = valor//1000
valor %= 1000
nota5 = valor//500
valor %= 500
nota2 = valor//200
valor %= 200

# Para cada moeda, calcula o resultado inteiro da divisão do valor
# por aquela moeda, armazena o resultado dessa divisão, que é o número
# de moedas que é possível devolver sem ultrapassar o valor informado,
# e, por fim, atualiza o novo valor para o que restou após trocar parte
# do valor pela moeda que acabou de ser calculada
moeda100 = valor//100
valor %= 100
moeda50 = valor//50
valor %= 50
moeda25 = valor//25
valor %= 25
moeda10 = valor//10
valor %= 10
moeda5 = valor//5
valor %= 5
moeda1 = valor

# Imprime os resultados obtidos

print("NOTAS:")
print("{:d} nota(s) de R$ 100.00".format(nota100))
print("{:d} nota(s) de R$ 50.00".format(nota50))
print("{:d} nota(s) de R$ 20.00".format(nota20))
print("{:d} nota(s) de R$ 10.00".format(nota10))
print("{:d} nota(s) de R$ 5.00".format(nota5))
print("{:d} nota(s) de R$ 2.00".format(nota2))

print("MOEDAS:")
print("{:d} moeda(s) de R$ 1.00".format(moeda100))
print("{:d} moeda(s) de R$ 0.50".format(moeda50))
print("{:d} moeda(s) de R$ 0.25".format(moeda25))
print("{:d} moeda(s) de R$ 0.10".format(moeda10))
print("{:d} moeda(s) de R$ 0.05".format(moeda5))
print("{:d} moeda(s) de R$ 0.01".format(moeda1))
