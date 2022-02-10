# Problema 1051 - Beecrowd - Iniciante - Nível 2

# Primeiramente, recebemos o valor da 'renda' digitado pelo usuário
# e iniciamos a variável 'imposto' com 0.00
renda = float(input())
imposto = 0.00

# Verificamos inicialmente, se o valor é maior que 2000.00, pois caso
# seja menor, não é necessário calcular o imposto
if renda <= 2000.00:
    print("Isento")

# Caso seja maior, retiramos o valor base de 2000.00 e calculamos o imposto
# de 8% sobre o valor restante. Porém, com um teto máximo de 1000.00
else:
    renda = renda - 2000.00
    if renda <= 1000.00:
        imposto = renda * 0.08
        print(f"R$ {imposto:.2f}")

    # Caso o restante da renda ultrapasse o teto da categoria atual, 
    # calculamos o imposto com base no teto dessa categoria e 
    # salvamos o restante para a próxima categoria de impostos, 
    # a categoria dos 18%, e é somado a variável 'imposto'
    else:
        imposto = 1000.00 * 0.08
        renda = renda - 1000.00
        if renda <= 1500.00:
            imposto += renda * 0.18
            print(f"R$ {imposto:.2f}")

        # Caso o restante da renda seja maior que o teto da categoria atual, 
        # todo o restante é calculado com base na nova categoria, a categoria
        #  de 28% e é somado a variável 'imposto'
        else:
            imposto += 1500.00 * 0.18
            renda = renda - 1500.00
            if renda > 0.00:
                imposto += renda * 0.28
            print(f"R$ {imposto:.2f}")