# Problema 1541 - Beecrowd - Iniciante - Nível 2

# Loop responsável pelos casos de testes
while True:
    # Leitura do caso de teste
    caso_teste = input()

    # Se 'caso_teste' for 0, a execução termina
    if caso_teste == "0":
        break

    # Convertendo os valores do caso de teste para Inteiros e
    # Separando os valores nas variáveis A, B e C
    A, B, C = [int(x) for x in caso_teste.split(" ")]
    percentual_do_terreno = C / 100

    # Calculando a área de ocupação da casa a ser construída
    area_da_casa = A * B

    # Calculando a área do terreno
    # Sabe-se que o percentual da área do terreno é igual a área da casa
    # Exemplo: 20% da area do terreno = area da casa, ou seja, area do terreno = area da casa / 0.2
    area_do_terreno = area_da_casa / percentual_do_terreno

    # Calculando a medida do lado do terreno
    # Os terrenos são perfeitamente quadrados, portanto, a área do terrenos é dada pela fórmula A = lado * lado
    # Consequentemente, lado = raiz quadrada de A
    lado_terreno = pow(area_do_terreno, 0.5)

    # Imprimindo o valor do lado do terreno
    print(int(lado_terreno))
