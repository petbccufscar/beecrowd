# Problema 2936 - URI - Iniciante - Nível 1

# Inicializa a quantidade de mandioca
# com a quantidade já conhecida, a parte
# que a dona Chica irá comer
Mandioca = 225

# Quantidade de convidados
Convidados = 5

# Laço de repetição que irá receber 5 valores
# em cada iteração, para saber quantas porções
# cada convidade irá comer
for i in range(Convidados):
    # Curupira
    if i == 0:
        Quantidade = int(input())
        Mandioca += Quantidade*300
    # Boitatá
    elif i == 1:
        Quantidade = int(input())
        Mandioca += Quantidade*1500
    # Boto
    elif i == 2:
        Quantidade = int(input())
        Mandioca += Quantidade*600
    # Mapinguari
    elif i == 3:
        Quantidade = int(input())
        Mandioca += Quantidade*1000
    # Iara
    else:
        Quantidade = int(input())
        Mandioca += Quantidade*150

print(Mandioca)
