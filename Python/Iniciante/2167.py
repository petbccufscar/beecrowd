#Problema 2167 - Beecrowd - Iniciante - Nível 2

#Recebe a quantidade de termos que irá ter e abaixo já recebe todos os termos
medida = int(input())
rpm = input().split()
i= 0
cont = 0

#Laço para fazer o teste com todos os termos, sendo medida -1 pois dendro do laço ele já compara
#com o termo posterior
while (i < medida - 1):

    #Compara o termo posterior com o termo anterior e se ele for maior o laço é quebrado
    if rpm[i+1] < rpm[i]:
        cont = i + 2
        break
    i += 1

#Imprime o resultado    
print(cont)