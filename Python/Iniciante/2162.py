# Problema 2162 - Beecrowd - Iniciante - Nível 4

# Entrada do número de medidas
input()

# Entrada das medidas em si
# Usamos compreensão de listas para converter cada entrada em int
medidas = [int(x) for x in input().split()]

# Vamos iterar par a par na lista
# zip() junta esses pares em uma lista de tuplas
# Que é desempacotada a cada iteração nas nossas
# variáveis.
pico = 0 # -1 vai representar que a última medição foi um vale
         # 1  representa um pico, e 0 é o valor inicial
for anterior, atual in zip(medidas, medidas[1:]):
    # Na primeira iteração temos que definir se estamos em um vale ou pico
    if (pico == 0):
        # Verificar se já não começamos num plano
        # Nesse caso paramos imediatamente
        if (anterior == atual): 
            print(0)
            exit()
        # Começamos em um pico
        if (anterior < atual): pico = 1
        # Começamos em um vale
        else: pico = -1
    else:
        # Estamos em um pico e o último foi um vale
        if (anterior < atual and pico == -1):
            pico = 1
        # Estamos em um vale e o último foi um pico
        elif (anterior > atual and pico == 1):
            pico = -1
        # Senão, algo deu errado e a paisagem não tem o padrão correto
        else:
            print(0)
            exit() # Sai do programa imediatamente, tornando o resto do código inacessível

# Se chegar aqui, deu tudo certo
print(1)
    
