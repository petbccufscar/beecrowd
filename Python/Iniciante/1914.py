#Problema 1914 - Beecrowd - Iniciante - Nível 2

#Recebe a quantidade de testes que o programa irá ter
testes = int(input())

i=1

#Faz o laço com a quantidade total de testes e é imprementado após sua execução
while i<=testes:

    #Recebe os nomes e a informação de quem escolheu par ou ímpar
    nomes = input().split()

    #Recebe os números que cada um jogou e após isso já faz a soma deles
    n1,n2 = map(int,input().split())
    soma = n1 + n2

    #Verifica se a soma é par ou ímpar
    if soma % 2 == 0:
        result = 'PAR'
    else:
        result = 'IMPAR'

    #Compara a primeira escolha de par/ímpar com o resultado e verifica se o primeiro jogador 
    #escolheu a mesma coisa, senão imprime o segundo jogador
    if result == nomes[1]:
        print(nomes[0])
    else:
        print(nomes[2])
    i += 1