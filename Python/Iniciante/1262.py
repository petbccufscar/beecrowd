while True:
    try:
        rastro = input()
        rastro = rastro.upper()
        processos = int(input())

        contador = 0
        ciclos = 0

        for i in rastro:
            if i == "R":
                contador += 1

                if contador == processos:
                    contador = 0
                    ciclos += 1
            elif i == "W" and contador != 0:
                contador = 0
                ciclos += 2
            elif i == "W":
                ciclos += 1

        if contador != 0:
            ciclos += 1

        print(ciclos)

    except EOFError:
        break
