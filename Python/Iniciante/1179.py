# Problema 1179 - Beecrowd - Iniciante - Nível 2

#inicializa os vetores vazios
par = []
impar = []

for i in range(15):

    #Recebe o valor de entrada
    Numeros = int(input())

    #Verifica se o valor é par ou impar e adiciona ele no vetor correspondente
    if Numeros % 2 == 0:
        par.append(Numeros)

    else:
        impar.append(Numeros)

    #Caso algum dos vetores chegue em 5, ele imprime os resultados e reseta o contador
    if len(par) == 5:
        cont = 0
        for a in par:
            print(f"par[{cont}] = {a}")
            cont += 1
        par = []

    if len(impar) == 5:

        cont = 0
        for b in impar:
            print(f"impar[{cont}] = {b}")
            cont += 1
        impar = []

#Imprime os valores que sobraram nos vetores ao final de tudo
if len(impar) > 0:
    cont = 0
    for b in impar:
        print(f"impar[{cont}] = {b}")
        cont += 1

if len(par) > 0:
    cont = 0
    for a in par:
        print(f"par[{cont}] = {a}")
        cont += 1