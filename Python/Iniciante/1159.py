# Problema 1159 - Beecrowd - Iniciante - Nível 1

while True: 
    x = int(input())
    y = x
    i = 0
    soma = 0
#Ponto de parada requisitado pelo exercício
    if(x == 0):
        break
#Verificando se o número é par, e caso sim, fazendo a soma dele com seus 4 pares seguintes   
    if(x % 2 == 0):
        for i in range(5):
            soma = soma + y
            y = y + 2
#Caso o número seja ímpar, ele é incrementado para virar par e é somado com os 4 pares seguintes
    else:
        y = y + 1
        for i in range(5):
            soma = soma + y
            y = y + 2
    print(soma)