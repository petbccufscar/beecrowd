#lendo o número de instâncias
num_instancias = int(input())
#para cada instância, lê a string original, e os erros dos times 1 e 2
for i in range(num_instancias):
    original = input()
    time_1 = input()
    time_2 = input()
    desempate = 0
    erros_1 = 0
    erros_2 = 0
    #compara as strings e conta os erros de cada time
    for c in range(len(original)):
        #se o time 1 errou
        if time_1[c] != original[c]:
            erros_1 += 1
            #se o time 1 errou, e o desempate ainda não foi definido, verifica se o time 2 acertou, se sim, o time 2 ganha no desempate
            if desempate == 0 and time_2[c] == original[c]:
                desempate = 2
        #se o time 2 errou
        if time_2[c] != original[c]:
            erros_2 += 1
            #se o time 2 errou, e o desempate ainda não foi definido, verifica se o time 1 acertou, se sim, o time 1 ganha no desempate
            if desempate == 0 and time_1[c] == original[c]:
                desempate = 1
                
    #imprime o resultado da instância
    print("Instancia %d" % (i + 1))
    if erros_1 < erros_2:
        print("time 1")
    elif erros_2 < erros_1:
        print("time 2")
    else:
        if desempate == 1:
            print("time 1")
        elif desempate == 2:
            print("time 2")
        else:
            print("empate")
    print()
