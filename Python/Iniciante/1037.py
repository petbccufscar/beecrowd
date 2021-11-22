# Problema 1037 - Beecrowd - Iniciante - Nível 3

# Recebe o valor
valor = float(input())

# Verifica em qual intervalo o valor está e imprime na sáida padrão
if 100 < valor:
    print("Fora de intervalo")
elif 75 < valor:
    print("Intervalo (75,100]")
elif 50 < valor:
    print("Intervalo (50,75]")
elif 25 < valor:
    print("Intervalo (25,50]")
elif 0 <= valor:
    print("Intervalo [0,25]")
else:
    print("Fora de intervalo")
