# Problema 1066 - URI - Iniciante - Nível 1

# Inicialização das variáveis com valor 0
par = 0
impar = 0
positivo = 0
negativo = 0

# 'for' para leitura dos argumentos
for num in range(5):
    num = int(input())
    # Assim que o argumento é recebido, é comparado se
    # o resto da divisão por 2 é zero, assim, sendo par
    if((num % 2) == 0):
        # Se for par, o valor de 'par' é incrementado em 1
        par += 1
    else:
        # Senão, o valor de 'impar' é incrementado em 1
        impar += 1
    if(num > 0):
        # Se for maior que 0, 'positivo' é incrementado em 1
        positivo += 1
    elif(num < 0):
        # Se for menor que 0, 'negativo' é incrementado em 1
        negativo += 1


# Imprime na tela a quantidade de cada com suas respectivas mensagens
print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')