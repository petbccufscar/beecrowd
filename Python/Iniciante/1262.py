# Problema 1262 - URI - Iniciante - Nível 2

# Loop que executa enquanto o input não terminar em EOF
while True:
    try:
        # Declaração e inicialização das variáveis por meio do input
        rastro = input()
        rastro = rastro.upper()
        processos = int(input())

        # controla a quantidade de operações de leitura
        # que foram feitas em sequência
        contador = 0
        # Controla a quantidade de ciclos completados
        ciclos = 0

        # Iteração sobre cada caractere presente no rastro informado
        for i in rastro:
            if i == "R":
                contador += 1

                # Verifica se completou um ciclo de leituras consecutivas
                if contador == processos:
                    contador = 0
                    ciclos += 1
            # Verifica se é uma operação de escrita logo após uma de leitura
            elif i == "W" and contador != 0:
                contador = 0
                ciclos += 2
            elif i == "W":
                ciclos += 1

        # Verifica se houve uma sequência de leituras,
        # mas que não ncessitou de um ciclo completo
        if contador != 0:
            ciclos += 1

        print(ciclos)

    # Caso em que o input chegou em EOF
    except EOFError:
        break
