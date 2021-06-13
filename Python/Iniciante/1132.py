# Problema 1132 - URI - Iniciante - Nível 1

# Entrada de dados
num_1 = int(input())
num_2 = int(input())

# Determinando qual é a maior entrada
if(num_2<num_1):
    i = num_2
    num_2 = num_1
    num_1 = i
    
# Cálculos para a saída, por uma laço de repetição testando se os números entre as entradas do usuário são divisíveis por 13
soma = 0
i = num_1
while(i<=num_2):
    if(i%13!=0):
        soma += i
    i+=1

# Saída esperada
print(soma)