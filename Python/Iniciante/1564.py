# Problema 1564 - Beecrowd - Iniciante - Nível 2

# Temos um loop que só se encerra, caso a entrada lida seja EOF
while True:
    try:
        # Recebemos o número de reclamações ao governo
        reclamacoes = int(input())

        # Caso o número de reclamações seja 0 (zero)
        if reclamacoes == 0:
            print("vai ter copa!")
        # Caso seja diferente de zero
        else:
            print("vai ter duas!")

    # Caso em que o input chegou em EOF
    except EOFError:
        break