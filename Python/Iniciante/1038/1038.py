# Problema 1038 - URI - Iniciante - Nível 1

#Declaração de variáveis, para item e a quantidade do item que será comprado.
entrada = input().split(' ') #Será feita uma lista com 2 espaços, sendo o primeiro qual tipo de item, e o segundo a quantidade deste.

#Distribuindo os valores de entrada em variáveis para melhor exemplificação.
item = int(entrada[0])
qtd_item = int(entrada[1])

#Estrutura condicional para escolher qual será o preço total cobrado.
if(item==1):
    preco = 4.00*qtd_item
elif(item==2):
    preco = 4.50*qtd_item
elif(item==3):
    preco = 5.00*qtd_item
elif(item==4):
    preco = 2.00*qtd_item
elif(item==5):
    preco = 1.50*qtd_item

print("Total: R$ %.2f" %preco)