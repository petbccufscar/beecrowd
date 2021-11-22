# Problema 1234 - Beecrowd - Strings - Nível 3

while True:
    try:
        # Leitura do texto
        sentence = input()
        result = ""

        # Controlador da alternância
        toggle = True

        # Para cada caractere no texto
        for i in sentence:
            # Se for uma letra
            if i.isalpha():
                # E tiver que ser maiúscula
                if toggle and i.islower():
                    # Adiciona a versão maiúscula dela
                    result += i.upper()
                # E tiver que ser minúscula
                elif not toggle and i.isupper():
                    # Adiciona a versão minúscula dela
                    result += i.lower()
                # E tiver certo
                else:
                    # Só adicionar
                    result += i

                toggle = not toggle
            # Se não for letra
            else:
                # Só adicionar
                result += i

        # Impressão do resultado
        print(result)

    except EOFError:
        break