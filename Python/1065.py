# Inicialização da variável 'par' com o valor 0
par = 0

# 'for' para leitura dos argumentos
for num in range(5):

    num = int(input())
    # Assim que o argumento é recebido, é comparado se
    # o resto da divisão por 2 é zero, assim, sendo par
    if((num % 2) == 0):
        # Se for par, o valor de 'par' é incrementado em 1
        par += 1

# Imprime na tela a quantidade de pares com o texto "valores pares"
print(par, "valores pares")
