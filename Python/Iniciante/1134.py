# Problema 1134 - URI - Iniciante - Nível 1

# Declaração de variáveis
combustivel = 1
qtd_alcool = 0
qtd_gasolina = 0
qtd_diesel = 0

# Entrada de dados até a digitação do digito 4
while(combustivel!=4):
    combustivel = int(input())
    if (combustivel==1):
        qtd_alcool +=1
    elif (combustivel==2):
        qtd_gasolina +=1
    elif (combustivel==3):
        qtd_diesel +=1


# Saída de dados
print(f"MUITO OBRIGADO\nAlcool: {qtd_alcool}\nGasolina: {qtd_gasolina}\nDiesel: {qtd_diesel}")