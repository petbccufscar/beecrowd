<<<<<<< HEAD
# Problema 1159 - Beecrowd - Iniciante - Nível 1

=======
>>>>>>> 24a72860fe18bc0289e6af7c79830aebb39cddd3
while True: 
    x = int(input())
    y = x
    i = 0
    soma = 0
<<<<<<< HEAD
#Ponto de parada requisitado pelo exercício
    if(x == 0):
        break
#Verificando se o número é par, e caso sim, fazendo a soma dele com seus 4 pares seguintes   
=======
    if(x == 0):
        break
>>>>>>> 24a72860fe18bc0289e6af7c79830aebb39cddd3
    if(x % 2 == 0):
        for i in range(5):
            soma = soma + y
            y = y + 2
<<<<<<< HEAD
#Caso o número seja ímpar, ele é incrementado para virar par e é somado com os 4 pares seguintes
=======
>>>>>>> 24a72860fe18bc0289e6af7c79830aebb39cddd3
    else:
        y = y + 1
        for i in range(5):
            soma = soma + y
            y = y + 2
<<<<<<< HEAD
    print(soma)
=======
    print(soma)
    if(x==0):
        break
>>>>>>> 24a72860fe18bc0289e6af7c79830aebb39cddd3
