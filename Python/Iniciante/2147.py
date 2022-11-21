# Problema 2060 - Beecrowd - Iniciante - Nível 2

#Recebe a quantidade de entradas que o teste terá
numero_testes = int(input())

#Realiza um loop até que sejam colocadas o número de entradas digitadas acima
for i in range(numero_testes):

    #Recebe a entrada e converse seus caracteres em uma quantidade numérica
    caracteres = len(input())
    
    #Mostra para o usuário quantos "segundos" demorou para digitar a quantidade de caracteres
    print("%.2f" % (caracteres*0.01))