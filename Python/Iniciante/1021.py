# Problema 1021 - URI - Iniciante - Nível 6

# Recebe o valor na entrada padrão
valor = float(input())

# Para cada cédula, calcula o resultado inteiro da divisão do valor
# por aquela cédula, armazena o resultado dessa divisão, que é o número
# de cédulas que é possível devolver sem ultrapassar o valor informado,
# e, por fim, atualiza o novo valor para o que restou após trocar parte
# do valor pela cédula que acabou de ser calculada
nota100 = int(valor/100)
valor -= nota100*100
nota50 = int(valor/50)
valor -= nota50*50
nota20 = int(valor/20)
valor -= nota20*20
nota10 = int(valor/10)
valor -= nota10*10
nota5 = int(valor/5)
valor -= nota5*5
nota2 = int(valor/2)
valor -= nota2*2

# Converte os centavos para um número inteiro
valor = int(valor*100)

# Para cada moeda, calcula o resultado inteiro da divisão do valor
# por aquela moeda, armazena o resultado dessa divisão, que é o número
# de moedas que é possível devolver sem ultrapassar o valor informado,
# e, por fim, atualiza o novo valor para o que restou após trocar parte
# do valor pela moeda que acabou de ser calculada
moeda100 = int(valor/100)
valor -= moeda100*100
moeda50 = int(valor/50)
valor -= moeda50*50
moeda25 = int(valor/25)
valor -= moeda25*25
moeda10 = int(valor/10)
valor -= moeda10*10
moeda5 = int(valor/5)
valor -= moeda5*5
moeda1 = int(valor)

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
