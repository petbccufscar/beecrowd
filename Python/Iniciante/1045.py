# Problema 1045 - Beecrowd - Iniciante - Nível 4

# Lendo os três valores do usuário com a função "input()", separando
# os valores pelo espaço, e ordenando os valores de modo decrescente
# com a função "sorted()".
lados = input().split()

ladoA, ladoB, ladoC = sorted(map(float, lados), reverse=True)

# Cálculo dos valores e mosta a saída do exercício.
if ladoA >= (ladoB + ladoC):
    print("NAO FORMA TRIANGULO")
else:
    if (ladoA * ladoA) == ((ladoB * ladoB) + (ladoC * ladoC)):
        print("TRIANGULO RETANGULO")
    elif (ladoA * ladoA) > ((ladoB * ladoB) + (ladoC * ladoC)):
        print("TRIANGULO OBTUSANGULO")
    elif (ladoA * ladoA) < ((ladoB * ladoB) + (ladoC * ladoC)):
        print("TRIANGULO ACUTANGULO")

    # Ajusta a lista com os valores dos lados e com a propriedade
    # ".count" podemos contar quantos lados possuem o valor passado,
    # assim testamos se há lados iguais.
    lados = [ladoA, ladoB, ladoC]

    if lados.count(ladoA) == 2 or lados.count(ladoB) == 2:
        print("TRIANGULO ISOSCELES")
    if lados.count(ladoA) == 3:
        print("TRIANGULO EQUILATERO")
