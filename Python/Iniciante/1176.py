#Problema 1176 - Beecrowd - Iniciante - Nível 3

#Definição da função fibonacci
def fibonacci(x):
    #Vetor iniciando com os valores de fib de 0 e 1
    fibos = [0, 1]
    for i in range(2, x+1):
        fibos.append(fibos[i-1] + fibos[i-2])
    return fibos[x]

#Leitura do número "T", que representa o número testes para o programa.
T = int(input())
 
#Criaçao do loop que repetirá o processo T vezes
for i in range(T):
    #Leitura do valor n a qual se quer saber o valor de fibonacci
    n = int(input())
    print(f"Fib({n}) = {fibonacci(n)}")