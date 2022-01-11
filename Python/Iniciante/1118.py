# Problema 1118 - Beecrowd - Iniciante - Nível 3

# Criando um loop while, para verificar a opção de novo cálculo ou não.
opcao = 1
while opcao == 1:

    # Entrada da nota 1.
    nota1 = float(input())

    # Validação da nota 1.
    while nota1 > 10 or nota1 < 0:
        print("nota invalida")
        nota1 = float(input())

    # Entrada da nota 2.
    nota2 = float(input())

    # Validação da nota 2.
    while nota2 > 10 or nota2 < 0:
        print("nota invalida")
        nota2 = float(input())

    # Apresentação da média, com duas casas decimais.
    print(f"media = {(nota1 + nota2) / 2:.2f}")

    # Solicitação de um novo cálculo de médias.
    opcao = int(input("novo calculo (1-sim 2-nao)\n"))

    # Validação da opção escolhida.
    while opcao != 1 and opcao != 2:
        opcao = int(input("novo calculo (1-sim 2-nao)\n"))
